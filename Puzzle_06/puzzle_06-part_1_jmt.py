""" Advent of code 2022 - Puzzle 06

    https://adventofcode.com/2022/day/06

    John Tocher     
    Solution to puzzle 06 part 1
"""

INPUT_FILE_NAME = "puzzle_06_input.txt"

running_list = list()

with open(INPUT_FILE_NAME, "r") as input_file:
    whole_line = input_file.read()  # The first read is the t=entirety of our input.
    for each_letter in whole_line:
        running_list.append(each_letter)
        if len(running_list) > 3:
            last_group = set(running_list[-4:])
            if len(last_group) == 4:
                print(f"Found init string after {len(running_list)} chars")
                break
        # print(f"{each_letter}", end="")

print(f"Result is: {len(running_list)}")
