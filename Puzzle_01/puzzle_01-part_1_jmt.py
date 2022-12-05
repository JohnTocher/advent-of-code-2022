""" Advent of code 2022 - Puzzle 01

    https://adventofcode.com/2022/day/1

    John Tocher     
    Solution to puzzle 01 part 1
"""

INPUT_FILE_NAME = "puzzle_01_input.txt"

this_total = 0  # We will re-use this variable for every elf as we iterate
max_total = 0   # This will store our largest total

with open(INPUT_FILE_NAME, "r") as input_file:
    for each_line in input_file:
        clean_line = each_line.strip()  # This removes any whitepace from both ends,but not the middle
        if clean_line:   # A string with any content at all is treated as True, an empty string is False
            line_as_number = int(clean_line)    # Converts text to an integer
            this_total += line_as_number
            if this_total > max_total:
                max_total = this_total
        else:   # A blank line - we need to reset the total for the next elf
            this_total = 0

print(f"The highest total found was {max_total}")
