f""" Advent of code 2022 - Puzzle 08

    https://adventofcode.com/2022/day/8

    John Tocher
    Solution to puzzle 08 part 2
"""

INPUT_FILE_NAME = "puzzle_08_input.txt"

tree_heights = dict()

row_num = 0  # We will use these to calculate x,y coordintates`
col_num = 0  # to act as keys for our dictionary, which will contain heights


def find_view_distance(tree_to_test, adjacent_trees, tree_data):
    """Takes the co-ordinates of one tree and checks how far to a blocked view

    A function lreally shouldn't operate on a global variable - in this case the
    tree-heights dictionary, I will show one solution for this by passing in that array in part 2"""

    tree_height = tree_data[tree_to_test]

    view_distance = 0
    for adjacent_tree in adjacent_trees:
        view_distance += 1
        if tree_data[adjacent_tree] >= tree_height:
            return view_distance

    return view_distance


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
best_view_score = 0

for row_num in range(2, forest_width):  # Loops don't reach the final value
    for col_num in range(2, forest_width):
        this_tree = (col_num, row_num)
        adjacent_trees = list()
        for col_adj in range(col_num - 1, 0, -1):  # left, from centre out
            adjacent_trees.append((col_adj, row_num))
        score_left = find_view_distance(this_tree, adjacent_trees, tree_heights)
        adjacent_trees = list()
        for col_adj in range(col_num + 1, forest_width + 1):  # right
            adjacent_trees.append((col_adj, row_num))
        score_right = find_view_distance(this_tree, adjacent_trees, tree_heights)
        adjacent_trees = list()
        for row_adj in range(row_num - 1, 0, -1):  # Trees above
            adjacent_trees.append((col_num, row_adj))
        score_above = find_view_distance(this_tree, adjacent_trees, tree_heights)
        adjacent_trees = list()
        for row_adj in range(row_num + 1, forest_width + 1):  # Trees below
            adjacent_trees.append((col_num, row_adj))
        score_below = find_view_distance(this_tree, adjacent_trees, tree_heights)
        view_score = score_above * score_right * score_left * score_below

        if view_score > best_view_score:
            best_view_score = view_score

print(f"Forest is: {forest_width} trees wide")
print(f"Best view score is {best_view_score}")
