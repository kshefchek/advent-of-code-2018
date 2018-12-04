import re
from typing import List, Union, NamedTuple


class Claim(NamedTuple):
    claim_id: int
    x_coordinate: int
    y_coordinate: int
    width: int
    height: int


def parse_claim(claim: str) -> Claim:
    claim_pattern = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')
    match = claim_pattern.fullmatch(claim)
    return Claim(
        claim_id=int(match.group(1)),
        x_coordinate=int(match.group(2)),
        y_coordinate=int(match.group(3)),
        width=int(match.group(4)),
        height=int(match.group(5))
    )


def map_claim(
        claim: Claim,
        claim_matrix: List[List[Union[int, str]]],
        ) -> bool:
    """
    side-effects - mutates claim_matrix
    updates claim matrix where
    0: no claim on square inch
    int (> 0): claimed, int is claim id
    'X': claimed by two elfs
    :return: True if there are overlaps else False
    """
    has_overlap = False
    for x_index in range(claim.x_coordinate, claim.x_coordinate + claim.width):
        for y_index in range(claim.y_coordinate, claim.y_coordinate + claim.height):
            if claim_matrix[y_index][x_index] == 0 \
                    or claim_matrix[y_index][x_index] == claim.claim_id:
                claim_matrix[y_index][x_index] = claim.claim_id
            else:
                has_overlap = True
                claim_matrix[y_index][x_index] = 'X'
    return has_overlap
