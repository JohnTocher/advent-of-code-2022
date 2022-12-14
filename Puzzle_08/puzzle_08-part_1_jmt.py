f""" Advent of code 2022 - Puzzle 08

    https://adventofcode.com/2022/day/8

    John Tocher
    Solution to puzzle 08 part 1
"""

INPUT_FILE_NAME = "puzzle_08_input.txt"

tree_heights = dict()

row_num = 0  # We will use these to calculate x,y coordintaes`
col_num = 0  # to act as keys for our dictionary, which will contain heights


def test_visibility(tree_to_test, adjacent_trees):
    """Takes the co-ordinates of one tree and checks if it's taller than a list of others

    A function lreally shouldn't operate on a global variable - in this case the
    tree-heights dictionary, I will show one solution for this by passing in that array in part 2"""

    tree_height = tree_heights[tree_to_test]
    visibility = True

    for adjacent_tree in adjacent_trees:
        if tree_heights[adjacent_tree] >= tree_height:
            visibility = False
            break

    return visibility


# Main program begins here

with open(INPUT_FILE_NAME, "r") as input_file:
    for each_line in input_file:
        row_num += 1
        col_num = 0
        clean_line = each_line.strip()  # Remove whitespace
        for each_char in clean_line:
            col_num += 1
            this_location = (col_num, row_num)  # A tuple like (4,3)
            this_height = int(each_char)
            tree_heights[this_location] = this_height

forest_width = row_num
interior_trees_visible = 0

for row_num in range(2, forest_width):  # Loops don't reach the final value
    for col_num in range(2, forest_width):
        this_tree = (col_num, row_num)
        adjacent_trees = list()
        for col_adj in range(1, col_num):  # left
            adjacent_trees.append((col_adj, row_num))
        clear_left = test_visibility(this_tree, adjacent_trees)
        adjacent_trees = list()
        for col_adj in range(col_num + 1, forest_width + 1):  # right
            adjacent_trees.append((col_adj, row_num))
        clear_right = test_visibility(this_tree, adjacent_trees)
        adjacent_trees = list()
        for row_adj in range(1, row_num):  # Trees above
            adjacent_trees.append((col_num, row_adj))
        clear_above = test_visibility(this_tree, adjacent_trees)
        adjacent_trees = list()
        for row_adj in range(row_num + 1, forest_width + 1):  # Trees below
            adjacent_trees.append((col_num, row_adj))
        clear_below = test_visibility(this_tree, adjacent_trees)

        if any((clear_above, clear_below, clear_left, clear_right)):
            interior_trees_visible += 1


print(f"Forest is: {forest_width} trees wide")
print(f"Found {interior_trees_visible} interior trees visible")
total_visible = 4 * forest_width - 4 + interior_trees_visible
print(f"{total_visible} total visible trees")
