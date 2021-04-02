import argparse
import time
from collections import namedtuple
import progressbar
import capnp
import capnp.lib.capnp
capnp.remove_import_hook()
import math
import json
import re
from distributed_bsc import BipartiteAdjacencyMatrix, find_bsc_par, \
        greedy_set_cover_with_complete_bipartite_subgraphs, \
        greed_set_cover_par
import gc
import multiprocessing
from reference_model import CompactArray, StructOfArray
import os.path
#from bokeh_plotting import create_plot_from_graph
from bitarray import bitarray

from node_lookup import NodeLookup
import reduce_graph_for_type
import sys
from optparse import OptionParser

"""
The purpose of this file is to execute the same things as build_patterns, but you can just kill it once instead of it just running endlessly.
  --node_to_wires --only_pips
  --wire_to_node
"""

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('--database', required=True)
    parser.add_argument('--output_dir')

    args = parser.parse_args()


    lookup = NodeLookup(database=args.database)
    cur = lookup.conn.cursor()


    cur.execute("SELECT name FROM tile_type ORDER BY name DESC;")
    all_tile_types = cur.fetchall()

    import subprocess
    #subprocess.check_output(['ls', '-l'])  # All that is technically needed...



    for num, row in enumerate(all_tile_types):
        for direction in ['node_to_wires_gs', 'node_to_pip_wires_gs', 'wire_to_node_gs']:
            tile_type = row[0]
            print(f'\n{num}. Working on: {tile_type} {direction}')
            subprocess.check_output(['make', direction, f'TILE={tile_type}'])



    # sys.argv.append('--node_to_wires')
    # sys.argv.append('--use_ms')
    # sys.argv.append('--set_start_method')
    # for num, row in enumerate(all_tile_types):
    #     tile_type = row[0]
    #     print(f'\n{num}. Working on: {tile_type}')
    #     sys.argv.append(f'--tile={tile_type}')
    #     reduce_graph_for_type.main()
    #     sys.argv.remove(f'--tile={tile_type}')
    #     if '--set_start_method' in sys.argv:
    #         sys.argv.remove('--set_start_method')


    return



if __name__ == "__main__":
    main()