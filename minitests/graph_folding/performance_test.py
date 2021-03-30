#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2017-2020  The Project X-Ray Authors.
#
# Use of this source code is governed by a ISC-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/ISC
#
# SPDX-License-Identifier: ISC

import argparse
import capnp
import capnp.lib.capnp
capnp.remove_import_hook()
import progressbar
import os.path
import time

from node_lookup import NodeLookup

from graph_lookup import WireToNodeLookup, NodeToWiresLookup


max_n2w_subgraphs = 0
max_w2n_subgraphs = 0
max_w2np_subgraphs = 0
max_subgraphs_type = {'n2w': 'none', 'w2n': 'none', 'w2np': 'none'}
database = {}
wire_list = []

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--database', required=True)
    parser.add_argument('--output_dir')

    args = parser.parse_args()

    graph_storage_schema = capnp.load('max_shared_storage.capnp')




    def read_tile_type_w2n(tile_type):
        print(f"read_tile_type_w2n for {tile_type}")
        return WireToNodeLookup(
            graph_storage_schema,
            os.path.join(
                args.output_dir, '{}_wire_to_nodes.bin'.format(tile_type)))

    def read_tile_type_n2w(tile_type):
        print(f"read_tile_type_n2w for {tile_type}")
        return NodeToWiresLookup(
            graph_storage_schema,
            os.path.join(
                args.output_dir, '{}_node_to_wires.bin'.format(tile_type)))

    def read_tile_type_n2w_pips_only(tile_type):
        print(f"read_tile_type_n2w_pips_only for {tile_type}")
        return NodeToWiresLookup(
            graph_storage_schema,
            os.path.join(
                args.output_dir, '{}_node_to_pip_wires.bin'.format(tile_type)))

    
    def load_database(cur):
        global wire_list
        this_tile = read_tile_type_n2w('HCLK_CMT')
        print('from db')
        for tile_pkey, wire_in_tile_pkey, node_pkey in progressbar.progressbar(cur.execute("""
SELECT tile_pkey, wire_in_tile_pkey, node_pkey FROM wire ORDER BY node_pkey;""")):
            wire_list.append([tile_pkey, wire_in_tile_pkey, node_pkey])
        # for tile_pkey, wire_in_tile_pkey, node_pkey in progressbar.progressbar(wire_list):
        #     another_wire_list.append(tile_pkey)
        # print('here')
        for tile_pkey, wire_in_tile_pkey, node_pkey in progressbar.progressbar(wire_list):
             pass
        exit()


    lookup = NodeLookup(database=args.database)
    cur = lookup.conn.cursor()
    #load_database(cur)

    tile_xy_to_tile_pkey = {}
    tile_pkey_to_xy = {}
    tile_pkey_to_tile_type_name = {}
    tile_type_to_wire_to_node_lookup = {}
    tile_type_to_node_to_wires_lookup = {}
    tile_type_to_node_to_pip_wires_lookup = {}

    for tile_pkey, tile_x, tile_y, tile_type_name in cur.execute("""
SELECT tile.pkey, tile.x, tile.y, tile_type.name
FROM tile
INNER JOIN tile_type ON tile.tile_type_pkey = tile_type.pkey;"""):
        tile_xy_to_tile_pkey[tile_x, tile_y] = tile_pkey
        tile_pkey_to_xy[tile_pkey] = (tile_x, tile_y)
        tile_pkey_to_tile_type_name[tile_pkey] = tile_type_name


    wire_in_tile_pkey_has_pip = set()
    for (wire_in_tile_pkey, ) in cur.execute("""
SELECT pkey FROM wire_in_tile WHERE has_pip_from;"""):
        wire_in_tile_pkey_has_pip.add(wire_in_tile_pkey)

    def check_node(node_pkey, current_node_elements):
        print(f"checking{node_pkey}")
        global max_n2w_subgraphs
        global max_w2n_subgraphs
        global max_w2np_subgraphs
        global max_subgraphs_type
        cur = lookup.conn.cursor()
        cur.execute(
            "SELECT tile_pkey, wire_in_tile_pkey FROM node WHERE pkey = ?",
            (node_pkey, ))
        node_tile_pkey, node_wire_in_tile_pkey = cur.fetchone()

        node_x, node_y = tile_pkey_to_xy[node_tile_pkey]

        any_errors = False
        #print(f"\nYou should remove {current_node_elements}")
        for tile_pkey, wire_in_tile_pkey in current_node_elements:
            #print(f"Checking tile_pkey:{tile_pkey}, wire_in_tile_pkey:{wire_in_tile_pkey}")
            wire_x, wire_y = tile_pkey_to_xy[tile_pkey]
            tile_type = tile_pkey_to_tile_type_name[tile_pkey]

            if tile_pkey==1 and wire_in_tile_pkey==12156:
                print('stop')
            if tile_type not in tile_type_to_wire_to_node_lookup:
                tile_type_to_wire_to_node_lookup[
                    tile_type] = read_tile_type_w2n(tile_type)

            lookup_node_x, lookup_node_y, lookup_node_wire_in_tile_pkey = tile_type_to_wire_to_node_lookup[
                tile_type].get_node(
                    tile_pkey, wire_x, wire_y, wire_in_tile_pkey)

            if (node_x, node_y,
                    node_wire_in_tile_pkey) != (lookup_node_x, lookup_node_y,
                                                lookup_node_wire_in_tile_pkey):
                print(
                    'ERROR: For ({}, {}), db ({}, {}, {}) != lookup ({}, {}, {})'
                    .format(
                        tile_pkey, wire_in_tile_pkey, node_x, node_y,
                        node_wire_in_tile_pkey, lookup_node_x, lookup_node_y,
                        lookup_node_wire_in_tile_pkey))
                any_errors = True

        current_node_elements_set = set(current_node_elements)
        leftover_node_elements = set(current_node_elements)

        node_tile_type = tile_pkey_to_tile_type_name[node_tile_pkey]
        if node_tile_type not in tile_type_to_node_to_wires_lookup:
            tile_type_to_node_to_wires_lookup[
                node_tile_type] = read_tile_type_n2w(node_tile_type)

        for wire_x, wire_y, wire_in_tile_pkey in tile_type_to_node_to_wires_lookup[
                node_tile_type].get_wires_for_node(
                    node_tile_pkey, node_x, node_y, node_wire_in_tile_pkey):
            tile_pkey = tile_xy_to_tile_pkey[wire_x, wire_y]
            assert (tile_pkey, wire_in_tile_pkey) in current_node_elements_set
            #print(f"Removing tile_pkey:{tile_pkey}, wire_in_tile_pkey:{wire_in_tile_pkey}")
            leftover_node_elements.remove((tile_pkey, wire_in_tile_pkey))

        #print(f"You still have {leftover_node_elements}")
        assert len(leftover_node_elements) == 0

        # Check pip only wires.
        pip_node_elements = set()

        if node_tile_type not in tile_type_to_node_to_pip_wires_lookup:
            tile_type_to_node_to_pip_wires_lookup[
                node_tile_type] = read_tile_type_n2w_pips_only(node_tile_type)

        for wire_x, wire_y, wire_in_tile_pkey in tile_type_to_node_to_pip_wires_lookup[
                node_tile_type].get_wires_for_node(
                    node_tile_pkey, node_x, node_y, node_wire_in_tile_pkey):
            tile_pkey = tile_xy_to_tile_pkey[wire_x, wire_y]
            assert (tile_pkey, wire_in_tile_pkey) in current_node_elements_set
            pip_node_elements.add((tile_pkey, wire_in_tile_pkey))

        for _, wire_in_tile_pkey in (
                current_node_elements_set - pip_node_elements):
            assert wire_in_tile_pkey not in wire_in_tile_pkey_has_pip

        return any_errors

    any_errors = False
    current_node_pkey = None
    current_node_elements = []
    total_ns = 0
    counter = 0
    for tile_pkey, wire_in_tile_pkey, node_pkey in progressbar.progressbar(
            cur.execute("""
SELECT tile_pkey, wire_in_tile_pkey, node_pkey FROM wire ORDER BY node_pkey;"""
                        )):
        
        start_time = time.perf_counter_ns()
        if current_node_pkey is None:
            current_node_pkey = node_pkey
        elif current_node_pkey != node_pkey:
            any_errors = check_node(#any_errors or check_node(
                current_node_pkey, current_node_elements)
            current_node_elements = []

        counter += 1
        current_node_pkey = node_pkey
        print(current_node_pkey)
        current_node_elements.append((tile_pkey, wire_in_tile_pkey))
        total_ns += time.perf_counter_ns() - start_time


    print(f"Total ns {total_ns}, Total minutes {total_ns/60000000000}, Total wires: {counter}")
    any_errors = any_errors or check_node(
        current_node_pkey, current_node_elements)

    global max_n2w_subgraphs
    global max_w2n_subgraphs
    global max_w2np_subgraphs
    global max_subgraphs_type
    print(f"Max node to wire subgraphs({max_subgraphs_type['n2w']}): {max_n2w_subgraphs}")
    print(f"Max wire to node subgraphs({max_subgraphs_type['w2n']}): {max_w2n_subgraphs}")
    print(f"Max wire to pip node subgraphs({max_subgraphs_type['w2np']}): {max_w2np_subgraphs}")
    #assert any_errors == False


if __name__ == "__main__":
    main()
