""" Advent of code 2022 - Puzzle 10

    https://adventofcode.com/2022/day/10

    John Tocher
    Solution to puzzle 10 part 1
"""

INPUT_FILE_NAME = "puzzle_10_input.txt"

reg_x = 1  # Iitialise our register
cycle_count = 1
add_stage = 0
cycle_record = dict()

with open(INPUT_FILE_NAME, "r") as input_file:
    for each_line in input_file:
        instruction = clean_line = each_line.strip()  # Remove whitespace
        # print(f"Cycle count {cycle_count:04} : x:{reg_x}")
        if instruction == "noop":
            cycle_record[cycle_count] = reg_x
            cycle_count += 1
        else:
            add_parts = instruction.split(" ")
            assert add_parts[0] == "addx", f"Unexpected instruction: {instruction}"
            val_to_add = int(add_parts[1])
            cycle_record[cycle_count] = reg_x
            cycle_count += 1
            cycle_record[cycle_count] = reg_x
            cycle_count += 1
            reg_x += val_to_add


skip_one = False
sum_of_strengths = 0
for cycle_num, reg_val in cycle_record.items():
    # print(f"Cycle count {cycle_num:04} : x:{reg_val}")
    sig_str = cycle_num * reg_val
    prev_reg_val = reg_val
    if (cycle_num % 20) == 0:
        if skip_one:
            skip_one = False
        else:
            print(f"End cycle {cycle_num:04} : x: {reg_val:04} sig str: {sig_str:04}")
            sum_of_strengths += sig_str
            skip_one = True
    else:
        # print(f"End cycle {cycle_num:04} : x: {reg_val:04} sig str: {sig_strength:04}")
        pass


print(f"Result is: {sum_of_strengths}")
