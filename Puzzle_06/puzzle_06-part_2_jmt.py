""" Advent of code 2022 - Puzzle 06

    https://adventofcode.com/2022/day/06

    John Tocher     
    Solution to puzzle 06 part 2
"""

INPUT_FILE_NAME = "puzzle_06_input.txt"

running_list = list()

with open(INPUT_FILE_NAME, "r") as input_file:
    whole_line = input_file.read()  # The first read is the entirety of our input.
    for each_letter in whole_line:
        # Strings are iterable, as they can be iterated/looped over as a series of characters
        running_list.append(each_letter)
        if len(running_list) >= 14:
            last_group = set(running_list[-14:])
            if len(last_group) == 14:
                # If there are 4 elemnents in a set, we have our sequence of 4 unique letters
                print(f"Found init string after {len(running_list)} chars")
                break  # No need to continue executing the loop now

print(f"Result is: {len(running_list)}")
