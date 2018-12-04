"""
Find two boxes of prototype fabric for santas new suit
https://adventofcode.com/2018/day/2
"""

import argparse
from puzzle_2.inventory_manager import checksum_ids, pairwise_alignment

parser = argparse.ArgumentParser()
parser.add_argument('--input', '-i', type=str, required=False,
                    default='./input/box_ids.txt')
args = parser.parse_args()

# 1 - get checksum to make sure we have all box ids
aoc_in = open(args.input, 'r')
box_ids = [line.rstrip() for line in aoc_in.readlines() if line.rstrip() != '']
print("Checksum for box ids: {}".format(checksum_ids(box_ids)))

# 2 - find ids with hamming distance of 1
for index, box_id in enumerate(box_ids):
    for query_id in box_ids[1:]:
        distance, alignment = pairwise_alignment(box_id, query_id)
        if distance == 1:
            print("Found similar ids with hamming distance of 1: {}".format(alignment))
    # shift list
    box_ids = box_ids[1:]
