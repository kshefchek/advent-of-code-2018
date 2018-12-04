import pytest
from puzzle_1.chronal_calibration import get_frequency, first_repeated_frequency

frequency_test_cases = [
    (
        [+1, +1, +1],
        3
    ),
    (
        [+1, +1, -2],
        0
    ),
    (
        [-1, -2, -3],
        -6
    )
]

@pytest.mark.parametrize("input_deltas, expected_frequency", frequency_test_cases)
def test_get_frequency(input_deltas, expected_frequency):
    """
    Test puzzle_1.chronal_calibration.get_frequency
    """
    ending_frequency = 0
    for freq in get_frequency(input_deltas, iterations=1):
        ending_frequency = freq
    assert ending_frequency == expected_frequency


repeated_frequency_cases = [
    (
        [+1, -1],
        0
    ),
    (
        [+3, +3, +4, -2, -4],
        10
    ),
    (
        [-6, +3, +8, +5, -6],
        5
    ),
    (
        [+7, +7, -2, -7, -4],
        14
    )
]


@pytest.mark.parametrize("input_deltas, expected_frequency", repeated_frequency_cases)
def test_get_first_repeat(input_deltas, expected_frequency):
    """
    test puzzle_1.chronal_calibration.first_repeated_frequency
    """
    repeat_freq = first_repeated_frequency(input_deltas, max_iterations=200)
    assert repeat_freq == expected_frequency
