import argparse
from puzzle_1.chronal_calibration import get_frequency, first_repeated_frequency

parser = argparse.ArgumentParser()
parser.add_argument('--input', '-i', type=str, required=False,
                    default='./input/freq_deltas.txt')
args = parser.parse_args()

aoc_in = open(args.input, 'r')
freq_deltas = [int(line.rstrip()) for line in aoc_in.readlines() if line.rstrip() != '']

# Problem 1 - What is the ending frequency after one iteration
ending_frequency = 0
for freq in get_frequency(freq_deltas, iterations=1):
    ending_frequency = freq

print("Ending frequency after one iteration: {}".format(ending_frequency))

# Problem 2 - What is the first repeated frequency
repeat_freq = first_repeated_frequency(freq_deltas, max_iterations=200)

print("First repeated frequency: {}".format(repeat_freq))