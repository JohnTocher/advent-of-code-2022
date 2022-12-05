""" Advent of code 2022 - Puzzle 03

    https://adventofcode.com/2022/day/3

    John Tocher     
    Solution to puzzle 03 part 2
"""

INPUT_FILE_NAME = "puzzle_03_input.txt"

priority_total = 0   # This will store our game total as per the rules
line_count = 0

list_of_rucksack_sets = list()  # Will end up containing a list of 3 sets

with open(INPUT_FILE_NAME, "r") as input_file:
    for each_line in input_file:
        clean_line = each_line.strip()  # This removes any whitepace from both ends,but not the middle
        unique_items = set(clean_line)
        list_of_rucksack_sets.append(unique_items)   # Add the set for each rucksack to the list
        line_count += 1         # Keep track of which sack of three we're counting
        if line_count == 3:     # we now have all three items
            common_item = set.intersection(*list_of_rucksack_sets)
            
            letter_ord = ord(common_item.pop()) # have to get the actual item left in the set, not the set itself
            if letter_ord >= 97:    # This is lower case, which have ord values of 97 to 122
                item_priority = letter_ord - 96 # 'a' with ord value 97 needs to be priority 1
            else:
                item_priority = letter_ord - 38 # 'A' with ord value 65 need to be 27
            priority_total += item_priority
            line_count = 0
            list_of_rucksack_sets = list()
         
print(f"Total prioriity for items in both compartments is: {priority_total}")
