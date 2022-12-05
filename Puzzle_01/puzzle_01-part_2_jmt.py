""" Advent of code 2022 - Puzzle 01

    https://adventofcode.com/2022/day/1

    John Tocher     
    Solution to puzzle 01 part 2
"""

INPUT_FILE_NAME = "puzzle_01_input.txt"

this_total = 0          # We will re-use this variable for every elf as we iterate
list_of_totals = list() # This creates an empty list. 

with open(INPUT_FILE_NAME, "r") as input_file:
    for each_line in input_file:
        clean_line = each_line.strip()  # This removes any whitepace from both ends,but not the middle
        if clean_line:   # A string with any content at all is treated as True, an empty string is False
            line_as_number = int(clean_line)    # Converts text to an integer
            this_total += line_as_number
        else:
            list_of_totals.append(this_total)   # Add this total the the end of the list
            this_total = 0                      # Reset the total for the next elf

list_of_totals.sort(reverse=True)   # Make descending, the default sort order is smallest to largest
sum_of_top_three = list_of_totals[0] + list_of_totals[1] + list_of_totals[2]

#print(f"List of totals is: {list_of_totals}")   # Uncomment this if you want to see the whole list
print(f"Top three add up to: {sum_of_top_three}")
