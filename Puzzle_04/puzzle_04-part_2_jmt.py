""" Advent of code 2022 - Puzzle 04

    https://adventofcode.com/2022/day/04

    John Tocher     
    Solution to puzzle 04 part 2
"""

INPUT_FILE_NAME = "puzzle_04_input.txt"

contained_pair_count = 0

with open(INPUT_FILE_NAME, "r") as input_file:

    for each_line in input_file:

        clean_line = each_line.strip()  # Remove whitespace
        pair_of_ranges = clean_line.split(",")  # Get A-B and X-Y as two strings

        # Split each of these strings "A-B" and "X-Y" into a list of two strings
        # Note that they still are strings, to do numeric comparison we have more to do

        list_left = pair_of_ranges[0].split("-")  # Now have a list ["A", "B"]
        list_right = pair_of_ranges[1].split("-")  # Now have a list ["X", "Y"]

        # We could use the same code as part 1 to do the integer conversion, but I'm
        # going to do it this time with a list comprehension
        range_a = [int(each_part) for each_part in list_left]
        range_b = [int(each_part) for each_part in list_right]

        if range_a[0] in range(range_b[0], range_b[1] + 1):
            contained_pair_count += 1
        elif range_a[1] in range(range_b[0], range_b[1] + 1):
            contained_pair_count += 1
        elif range_b[0] in range(range_a[0], range_a[1] + 1):
            contained_pair_count += 1
        elif range_b[1] in range(range_a[0], range_a[1] + 1):
            contained_pair_count += 1

print(f"Result is: {contained_pair_count}")
