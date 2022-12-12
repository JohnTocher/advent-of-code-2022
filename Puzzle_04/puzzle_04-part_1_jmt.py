""" Advent of code 2022 - Puzzle 04

    https://adventofcode.com/2022/day/04

    John Tocher     
    Solution to puzzle 04 part 1
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

        # We could (and I did initially) fit the integter conversion into our logical
        # if statements, but it's more readable to do it as a separate step

        range_a = [int(list_left[0]), int(list_left[1])]  # Convert to integers
        range_b = [int(list_right[0]), int(list_right[1])]  # ["1", "2"] becomes [1, 2]

        # For [A, B] and [X, Y] we now do our checks to see which is inside which, if any
        if range_a[0] >= range_b[0] and range_a[1] <= range_b[1]:
            contained_pair_count += 1  # [A, B] is inside [X, Y]
        elif range_b[0] >= range_a[0] and range_b[1] <= range_a[1]:
            contained_pair_count += 1  # [X, Y] is inside [A, B]

print(f"Result is: {contained_pair_count}")
