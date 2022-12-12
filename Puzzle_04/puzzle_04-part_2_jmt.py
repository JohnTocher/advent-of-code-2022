""" Advent of code 2022 - Puzzle 04

    https://adventofcode.com/2022/day/04

    John Tocher     
    Solution to puzzle 04 part 2
"""

INPUT_FILE_NAME = "puzzle_04_input.txt"

contained_pair_count = 0

with open(INPUT_FILE_NAME, "r") as input_file:
    for each_line in input_file:
        clean_line = (
            each_line.strip()
        )  # This removes any whitepace from both ends,but not the middle
        pair_of_ranges = clean_line.split(",")
        range_a = [
            int(this_entry) for this_entry in pair_of_ranges[0].split("-")
        ]  # The 1st of the previous list, split into another list
        range_b = [
            int(this_entry) for this_entry in pair_of_ranges[1].split("-")
        ]  # The 2nd of the previous list, split into another list

        print(f"Input: {clean_line} maps to {range_a} and {range_b}")
        if range_a[0] in range(range_b[0], range_b[1] + 1):
            contained_pair_count += 1
        elif range_a[1] in range(range_b[0], range_b[1] + 1):
            contained_pair_count += 1
        elif range_b[0] in range(range_a[0], range_a[1] + 1):
            contained_pair_count += 1
        elif range_b[1] in range(range_a[0], range_a[1] + 1):
            contained_pair_count += 1

print(f"Result is: {contained_pair_count}")
