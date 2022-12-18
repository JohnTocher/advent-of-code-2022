""" Advent of code 2022 - Puzzle 10

    https://adventofcode.com/2022/day/10

    John Tocher
    Solution to puzzle 10 part 2
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


pixel_pos = 0
sprite_pos = 1
cycle_num = 1
this_line = ""

for cycle_num, reg_val in cycle_record.items():

    sprite_pos = reg_val
    sprite_range = range(reg_val - 1, reg_val + 2)

    draw_symbol = "."
    if pixel_pos in sprite_range:
        draw_symbol = "#"
    this_line = f"{this_line}{draw_symbol}"

    if (cycle_num % 40) == 0:
        print(f"{this_line} {cycle_num}")
        this_line = ""

    pixel_pos += 1
    if pixel_pos == 40:
        pixel_pos = 0

print(f"Result is printed in debug output")
