""" Advent of code 2022 - Puzzle 03

    https://adventofcode.com/2022/day/3

    John Tocher     
    Solution to puzzle 03 part 1
"""

INPUT_FILE_NAME = "puzzle_03_input.txt"

priority_total = 0   # This will store our game total as per the rules

with open(INPUT_FILE_NAME, "r") as input_file:
    for each_line in input_file:
        clean_line = each_line.strip()  # This removes any whitepace from both ends,but not the middle
        comp_size = int(len(clean_line) / 2)  # Compartments are each half the size of rucksack
        # ToDo - check that we have an even number of items even though we can function on an odd number

        compartment_A = clean_line[0:comp_size]    # For example for "AbCd" (length 4) we need 0:2 and 2:4
        compartment_B = clean_line[comp_size:]      # The open ended range means to go right to the end

        for each_item in compartment_A:
            if each_item in compartment_B:  # If true we have found our packing failure
                letter_ord = ord(each_item)
                if letter_ord >= 97:    # This is lower case, which have ord values of 97 to 122
                    item_priority = letter_ord - 96 # 'a' with ord value 97 needs to be priority 1
                else:
                    item_priority = letter_ord - 38 # 'A' with ord value 65 need to be 27
                priority_total += item_priority
                break   # We can stop searching for the common item now - we only want to count it once
            
print(f"Total prioriity for items in both compartments is: {priority_total}")
