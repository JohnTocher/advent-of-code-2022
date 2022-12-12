""" Advent of code 2022 - Puzzle 04

    https://adventofcode.com/2022/day/04

    John Tocher     
    Solution to puzzle 04 part 1
"""

INPUT_FILE_NAME = "puzzle_04_input.txt"

contained_pair_count = 0

with open(INPUT_FILE_NAME, "r") as input_file:
    for each_line in input_file:
        clean_line = (
            each_line.strip()
        )  # This removes any whitepace from both ends,but not the middle
        pair_of_ranges = clean_line.split(",")
        range_a = pair_of_ranges[0].split(
            "-"
        )  # The 1st of the previous list, split into another list
        range_b = pair_of_ranges[1].split(
            "-"
        )  # The 2nd of the previous list, split into another list

        if int(range_a[0]) >= int(range_b[0]) and int(range_a[1]) <= int(range_b[1]):
            contained_pair_count += 1
        elif int(range_b[0]) >= int(range_a[0]) and int(range_b[1]) <= int(range_a[1]):
            contained_pair_count += 1

print(f"Result is: {contained_pair_count}")
