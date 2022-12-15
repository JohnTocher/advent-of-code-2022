""" Advent of code 2022 - Puzzle 09

    https://adventofcode.com/2022/day/9

    John Tocher
    Solution to puzzle 09 part 2A - sigh, alternate version coz I forgot to git push from home
"""

INPUT_FILE_NAME = "puzzle_09_input_tiny.txt"


def get_move_values(which_dir):
    """return the dela values for X and Y based on direction

    Assuming right and up are the positive directions
    """

    if which_dir == "L":
        return (-1, 0)
    elif which_dir == "R":
        return (1, 0)
    elif which_dir == "U":
        return (0), 1
    elif which_dir == "D":
        return (0, -1)
    else:
        return False


def move_point(point_pos, delta_values):
    """Update the X and Y components of point pos with the delta values provided"""

    x_pos = point_pos[0] + delta_values[0]
    y_pos = point_pos[1] + delta_values[1]

    return (x_pos, y_pos)


def calc_move_values(head_pos, tail_pos):
    """Caclulate the delta X and Y for the two points accoriding to our rules"""

    dx = head_pos[0] - tail_pos[0]
    dy = head_pos[1] - tail_pos[1]

    abs_sum = abs(dx) + abs(dy)

    if abs_sum in (0, 1):  # Touching, don't move
        return (0, 0)

    if abs(dx) == 1 and abs(dy) == 1:
        return (0, 0)  # Touching diagoinal

    if abs(dx) == 2:  # Two apart in x
        if dy == 0:  # Same column
            return (int(dx / 2), 0)
        elif dy == 2:  # Off two in each direction, couldn't happen with small example
            return (int(dx / 2), int(dy / 2))
        else:  # Different columns - move diagonal
            return (int(dx / 2), dy)

    if abs(dy) == 2:  # Two apart in Y
        if dx == 0:  # Same row
            return (0, int(dy / 2))
        elif dx == 2:  # Off two in each direction, couldn't happen with small example
            return (int(dx / 2), int(dy / 2))
        else:
            return (dx, int(dy / 2))

    print(f"DX:{dx}, DY:{dy}")
    assert False, f"Unexpected distance apart: {head_pos} and {tail_pos}"


head_pos = (0, 0)
tail_pos = (0, 0)
tail_history = list()

with open(INPUT_FILE_NAME, "r") as input_file:
    for each_line in input_file:
        clean_line = each_line.strip()  # Remove whitespace
        which_dir, hop_count_text = clean_line.split(" ")
        hops_to_do = int(hop_count_text)
        # print(f"Going {which_dir} for {hops_to_do} steps")
        for hop_count in range(0, hops_to_do):
            move_values = get_move_values(which_dir)
            head_pos = move_point(head_pos, move_values)
            tail_shift = calc_move_values(head_pos, tail_pos)
            tail_pos = move_point(tail_pos, tail_shift)
            tail_history.append(tail_pos)
            # print(f"After {which_dir} head is at {head_pos}, tail at {tail_pos}")

tail_positions = len(set(tail_history))

print(f"Result is: {tail_positions} tail positions")
