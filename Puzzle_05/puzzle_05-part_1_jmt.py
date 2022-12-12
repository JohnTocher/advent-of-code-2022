""" Advent of code 2022 - Puzzle 05

    https://adventofcode.com/2022/day/05

    John Tocher     
    Solution to puzzle 05 part 1
"""

INPUT_FILE_NAME = "puzzle_05_input.txt"


def get_stack_states():
    """Return the initial condition of the stacks

    Each stack is modelled a list, with the first item
    in the list rperesenting the bottom-most item

    the stacks as a group are stored in a dictionary,
    with the keys being the stack numebers
    """

    all_stacks = dict()
    all_stacks[1] = list("PFMQWGRT")
    all_stacks[2] = list("HFR")
    all_stacks[3] = list("PZRVGHSD")
    all_stacks[4] = list("QHPBFWG")
    all_stacks[5] = list("PSMJH")
    all_stacks[6] = list("MZTHSRPL")
    all_stacks[7] = list("PTHNML")
    all_stacks[8] = list("FDQR")
    all_stacks[9] = list("DSCNLPH")

    return all_stacks


stack_state = get_stack_states()

with open(INPUT_FILE_NAME, "r") as input_file:
    for each_line in input_file:
        clean_line = (
            each_line.strip()
        )  # This removes any whitepace from both ends,but not the middle
        if clean_line.startswith("move"):

            # The index of the letter where the word from appears
            pos_from = clean_line.find("from")
            # The index of the letter where the word from appears
            pos_to = clean_line.find("to")

            # get the integer values of the three things we need for each move
            number_to_move = int(clean_line[4:pos_from])
            stack_from = int(clean_line[pos_from + 4 : pos_to])
            stack_to = int(clean_line[pos_to + 2 :])

            # Iterating the number of crates we have to move
            for stack_count in range(0, number_to_move):
                crate_to_move = stack_state[stack_from].pop()
                stack_state[stack_to].append(crate_to_move)

# Now we will manally loop over the stack state to get the top item of each
final_result = ""  # An empty string
for stack_number in range(1, 10):  # There are nine crates, it will stop before 10
    # print(f"Stack {stack_number} is {stack_state[stack_number]}")
    this_crate = stack_state[stack_number].pop()
    final_result += this_crate

print(f"Result is: {final_result}")
