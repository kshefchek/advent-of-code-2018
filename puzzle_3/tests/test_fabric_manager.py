from puzzle_3.fabric_manager import map_claim, parse_claim, Claim
import pytest

test_data = [
    (
        '#1 @ 1,3: 4x4',
        Claim(
            claim_id=1,
            x_coordinate=1,
            y_coordinate=3,
            width= 4,
            height=4
        )
    ),
    (
        '#2 @ 3,1: 4x4',
        Claim(
            claim_id=2,
            x_coordinate=3,
            y_coordinate=1,
            width=4,
            height=4
        )
    ),
    (
        '#3 @ 5,5: 2x2',
        Claim(
            claim_id=3,
            x_coordinate=5,
            y_coordinate=5,
            width=2,
            height=2
        )
    )
]


@pytest.mark.parametrize("claim_string, expected_claim", test_data)
def test_parse_claims(claim_string, expected_claim):
    """
    test parse_claims
    """
    claim = parse_claim(claim_string)
    assert claim == expected_claim


def test_map_claims():
    """
    test puzzle_3.fabric_manager.map_claims
    """
    test_data = [
        Claim(1, 1, 3, 4, 4),
        Claim(2, 3, 1, 4, 4),
        Claim(3, 5, 5, 2, 2)
    ]
    expected_matrix = [
        [0, 0, 0,  0,   0,  0, 0, 0, 0],
        [0, 0, 0,  2,   2,  2, 2, 0, 0],
        [0, 0, 0,  2,   2,  2, 2, 0, 0],
        [0, 1, 1, 'X', 'X', 2, 2, 0, 0],
        [0, 1, 1, 'X', 'X', 2, 2, 0, 0],
        [0, 1, 1,  1,   1,  3, 3, 0, 0],
        [0, 1, 1,  1,   1,  3, 3, 0, 0],
        [0, 0, 0,  0,   0,  0, 0, 0, 0],
        [0, 0, 0,  0,   0,  0, 0, 0, 0]
    ]

    claim_matrix = [[0 for x in range(9)] for y in range(9)]
    for claim in test_data:
        map_claim(claim, claim_matrix)
    assert claim_matrix == expected_matrix
