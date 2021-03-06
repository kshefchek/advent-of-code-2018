import pytest
from puzzle_2.inventory_manager import checksum_ids, pairwise_alignment

checksum_test_cases = [
    (
        [
            'abcdef',
            'bababc',
            'abbcde',
            'abcccd',
            'aabcdd',
            'abcdee',
            'ababab'
        ],
        12
    ),
]


@pytest.mark.parametrize("box_ids, expected_checksum", checksum_test_cases)
def test_checksum(box_ids, expected_checksum):
    """
    test puzzle_2.inventory_manager.checksum_ids
    """
    assert checksum_ids(box_ids) == expected_checksum


def test_pairwise_alignment():
    """
    test puzzle_2.inventory_manager.pairwise_alignment
    """
    expected_distance = 1
    expected_alignment = 'fg*ij'
    distance, alignment = pairwise_alignment('fghij', 'fguij')
    assert distance == expected_distance
    assert alignment == expected_alignment
