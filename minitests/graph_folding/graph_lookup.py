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

from reference_model import CompactArray


class WireToNodeLookup():
    def __init__(self, schema, wire_to_node_patterns_fname):
        with open(wire_to_node_patterns_fname, 'rb') as f:
            self.wire_to_node_capnp = schema.WireToNodeStorage.read(f)

        # self.wire_in_tile_pkeys = CompactArray()
        # self.wire_in_tile_pkeys.read_from_capnp(
        #     self.wire_to_node_capnp.wireInTilePkeys)

        self.node_pattern_dx = CompactArray()
        self.node_pattern_dx.read_from_capnp(
            self.wire_to_node_capnp.nodePatternDx)

        self.node_pattern_dy = CompactArray()
        self.node_pattern_dy.read_from_capnp(
            self.wire_to_node_capnp.nodePatternDy)

        self.node_pattern_to_node_wire = CompactArray()
        self.node_pattern_to_node_wire.read_from_capnp(
            self.wire_to_node_capnp.nodePatternToNodeWire)

        # self.subgraphs = []
        # for subgraph_capnp in self.wire_to_node_capnp.subgraphs:
        #     subgraph = CompactArray()
        #     subgraph.read_from_capnp(subgraph_capnp)
        #     self.subgraphs.append(subgraph)


        self.wire_in_tile_pkeys = []
        for wire_in_tile_pkeys_capnp in self.wire_to_node_capnp.wireInTilePkeys:
            wire_in_tile_pkey = CompactArray()
            wire_in_tile_pkey.read_from_capnp(wire_in_tile_pkeys_capnp)
            self.wire_in_tile_pkeys.append(wire_in_tile_pkey)

        self.keys_to_pattern = []
        for keys_to_pattern_capnp in self.wire_to_node_capnp.keysToPattern:
            key_to_pattern = CompactArray()
            key_to_pattern.read_from_capnp(keys_to_pattern_capnp)
            self.keys_to_pattern.append(key_to_pattern)

        # self.tile_patterns = []
        # for tile_pattern_capnp in self.wire_to_node_capnp.tilePatterns:
        #     tile_pattern = CompactArray()
        #     tile_pattern.read_from_capnp(tile_pattern_capnp)

        #     for subgraph_idx in tile_pattern.items:
        #         assert subgraph_idx < len(self.subgraphs)

        #     self.tile_patterns.append(tile_pattern)

        self.tile_pkeys = CompactArray()
        self.tile_pkeys.read_from_capnp(self.wire_to_node_capnp.tilePkeys)

        # tile_to_tile_patterns = CompactArray()
        # tile_to_tile_patterns.read_from_capnp(
        #     self.wire_to_node_capnp.tileToTilePatterns)

        # self.tile_to_tile_patterns = {}

        # for tile_pkey, tile_pattern_idx in zip(tile_pkeys.items,
        #                                        tile_to_tile_patterns.items):
        #     assert tile_pattern_idx < len(
        #         self.tile_patterns), wire_to_node_patterns_fname
        #     self.tile_to_tile_patterns[tile_pkey] = tile_pattern_idx

    def get_node(self, tile_pkey, x, y, wire_in_tile_pkey):
        tile_idx = self.tile_pkeys.index_get(tile_pkey)
        wire_idx = self.wire_in_tile_pkeys[tile_idx].index_get(wire_in_tile_pkey)
        # wire_idx = self.wire_in_tile_pkeys.index_get(wire_in_tile_pkey, None)
        if wire_idx is None:
            # This is already the node!
            return x, y, wire_in_tile_pkey

        node_pattern_idx = self.keys_to_pattern[tile_idx].items[wire_idx]
        node_x = x + self.node_pattern_dx.items[node_pattern_idx]
        node_y = y + self.node_pattern_dy.items[node_pattern_idx]
        node_wire_in_tile_pkey = self.node_pattern_to_node_wire.items[
            node_pattern_idx]

        return node_x, node_y, node_wire_in_tile_pkey


        print('here')

        # tile_pattern_idx = self.tile_to_tile_patterns[tile_pkey]
        # tile_pattern = self.tile_patterns[tile_pattern_idx]

        # node_pattern_idx = None
        # for subgraph_idx in tile_pattern.items:
        #     subgraph = self.subgraphs[subgraph_idx]

        #     if subgraph.items[wire_idx] is not None:
        #         node_pattern_idx = subgraph.items[wire_idx]
        #         break

        # if node_pattern_idx is None:
        #     # This is already the node!
        #     return x, y, wire_in_tile_pkey

        # node_x = x + self.node_pattern_dx.items[node_pattern_idx]
        # node_y = y + self.node_pattern_dy.items[node_pattern_idx]
        # node_wire_in_tile_pkey = self.node_pattern_to_node_wire.items[
        #     node_pattern_idx]

        # return node_x, node_y, node_wire_in_tile_pkey


class NodeToWiresLookup():
    def __init__(self, schema, node_to_wires_fname):
        with open(node_to_wires_fname, 'rb') as f:
            self.node_to_wires_capnp = schema.NodeToWiresStorage.read(f)

        # self.node_wire_in_tile_pkeys = CompactArray()
        # self.node_wire_in_tile_pkeys.read_from_capnp(
        #     self.node_to_wires_capnp.nodeWireInTilePkeys)

        self.wire_pattern_dx = CompactArray()
        self.wire_pattern_dx.read_from_capnp(
            self.node_to_wires_capnp.wirePatternDx)

        self.wire_pattern_dy = CompactArray()
        self.wire_pattern_dy.read_from_capnp(
            self.node_to_wires_capnp.wirePatternDy)

        self.wire_pattern_to_wire = CompactArray()
        self.wire_pattern_to_wire.read_from_capnp(
            self.node_to_wires_capnp.wirePatternToWire)

        self.node_patterns = []
        for node_pattern_capnp in self.node_to_wires_capnp.nodePatterns:
            node_pattern = CompactArray()
            node_pattern.read_from_capnp(node_pattern_capnp)
            self.node_patterns.append(node_pattern)

        # self.subgraphs = []
        # for subgraph_capnp in self.node_to_wires_capnp.subgraphs:
        #     subgraph = CompactArray()
        #     subgraph.read_from_capnp(subgraph_capnp)
        #     self.subgraphs.append(subgraph)


        self.node_wire_in_tile_pkeys = []
        for node_wire_in_tile_pkeys_capnp in self.node_to_wires_capnp.nodeWireInTilePkeys:
            node_wire_in_tile_pkey = CompactArray()
            node_wire_in_tile_pkey.read_from_capnp(node_wire_in_tile_pkeys_capnp)
            self.node_wire_in_tile_pkeys.append(node_wire_in_tile_pkey)


        self.keys_to_patterns = []
        for keys_to_patterns_capnp in self.node_to_wires_capnp.keysToPatterns:
            keys_to_pattern = CompactArray()
            keys_to_pattern.read_from_capnp(keys_to_patterns_capnp)
            self.keys_to_patterns.append(keys_to_pattern)

        # self.tile_patterns = []
        # for tile_pattern_capnp in self.node_to_wires_capnp.tilePatterns:
        #     tile_pattern = CompactArray()
        #     tile_pattern.read_from_capnp(tile_pattern_capnp)

        #     for subgraph_idx in tile_pattern.items:
        #         assert subgraph_idx < len(self.subgraphs)

        #     self.tile_patterns.append(tile_pattern)

        self.tile_pkeys = CompactArray()
        self.tile_pkeys.read_from_capnp(self.node_to_wires_capnp.tilePkeys)

        # tile_to_tile_patterns = CompactArray()
        # tile_to_tile_patterns.read_from_capnp(
        #     self.node_to_wires_capnp.tileToTilePatterns)

        # self.tile_to_tile_patterns = {}

        # for tile_pkey, tile_pattern_idx in zip(tile_pkeys.items,
        #                                        tile_to_tile_patterns.items):
        #     assert tile_pattern_idx < len(
        #         self.tile_patterns), node_to_wires_fname
        #     self.tile_to_tile_patterns[tile_pkey] = tile_pattern_idx

    def get_wires_for_node(self, tile_pkey, x, y, node_wire_in_tile_pkey):
        yield (x, y, node_wire_in_tile_pkey)

        tile_idx = self.tile_pkeys.index_get(tile_pkey)
        wire_idx = self.node_wire_in_tile_pkeys[tile_idx].index_get(node_wire_in_tile_pkey)
        # wire_idx = self.wire_in_tile_pkeys.index_get(wire_in_tile_pkey, None)
        if wire_idx is None:
            # This is already the node!
            return x, y, node_wire_in_tile_pkey


        node_pattern_idx = self.keys_to_patterns[tile_idx].items[wire_idx]

        for wire_pattern_idx in self.node_patterns[node_pattern_idx].items:
            wire_x = x + self.wire_pattern_dx.items[wire_pattern_idx]
            wire_y = y + self.wire_pattern_dy.items[wire_pattern_idx]
            wire_in_tile_pkey = self.wire_pattern_to_wire.items[
                wire_pattern_idx]

            yield wire_x, wire_y, wire_in_tile_pkey



        node_wire_idx = self.node_wire_in_tile_pkeys.index_get(
            node_wire_in_tile_pkey, None)
        if node_wire_idx is None:
            # This node is only itself!
            return

        tile_pattern_idx = self.tile_to_tile_patterns[tile_pkey]
        tile_pattern = self.tile_patterns[tile_pattern_idx]

        node_pattern_idx = None
        for subgraph_idx in tile_pattern.items:
            subgraph = self.subgraphs[subgraph_idx]

            if subgraph.items[node_wire_idx] is not None:
                node_pattern_idx = subgraph.items[node_wire_idx]
                break

        if node_pattern_idx is None:
            # This node is only itself!
            return

        for wire_pattern_idx in self.node_patterns[node_pattern_idx].items:
            wire_x = x + self.wire_pattern_dx.items[wire_pattern_idx]
            wire_y = y + self.wire_pattern_dy.items[wire_pattern_idx]
            wire_in_tile_pkey = self.wire_pattern_to_wire.items[
                wire_pattern_idx]

            yield wire_x, wire_y, wire_in_tile_pkey