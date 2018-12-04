import argparse
from puzzle_3.fabric_manager import map_claim, parse_claim

parser = argparse.ArgumentParser()
parser.add_argument('--input', '-i', type=str, required=False,
                    default='./input/claims.txt')
args = parser.parse_args()

aoc_in = open(args.input, 'r')
claim_list = [line.rstrip() for line in aoc_in.readlines() if line.rstrip() != '']

claim_matrix = [[0 for x in range(1100)] for y in range(1100)]

for clm in claim_list:
    claim = parse_claim(clm)
    map_claim(claim, claim_matrix)


# 1 - How many square inches have overlapping claims?

print("{} square inches have overlaps".format(
    sum([1 for row in claim_matrix for field in row if field == 'X'])
))

# 2 - What claim is not overlapping with any others?
for clm in claim_list:
    claim = parse_claim(clm)
    has_overlap = map_claim(claim, claim_matrix)
    if not has_overlap:
        print("claim {} has no overlaps".format(claim.claim_id))
