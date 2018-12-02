from typing import List, Iterator

# https://adventofcode.com/2018/day/1

def get_frequency(deltas: List, iterations: int) -> Iterator[int]:
    frequency = 0
    num_iterations = 0
    yield frequency
    while num_iterations < iterations:
        num_iterations += 1
        for delta in deltas:
            frequency += delta
            yield frequency


def first_repeated_frequency(deltas: List, max_iterations: int) -> int:
    """
    Returns the first repeated frequency, or None if no frequencies
    are repeated within max iterations
    """
    frequencies = set()  # cached frequencies
    first_repeated_freq = None

    for frequency in get_frequency(deltas, iterations=max_iterations):

        if frequency in frequencies:
            first_repeated_freq = frequency
            break

        frequencies.add(frequency)

    return first_repeated_freq
