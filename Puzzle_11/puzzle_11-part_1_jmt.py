""" Advent of code 2022 - Puzzle 11

    https://adventofcode.com/2022/day/11

    John Tocher
    Solution to puzzle 11 part 1
"""
1
INPUT_FILE_NAME = "puzzle_11_input_small.txt"


def read_monkey_data(verbose_output=False):
    """Reads the initial info on the monkeys from the puzzle input"""

    monkey_stats = dict()
    current_monkey_details = dict()
    current_monkey_number = False

    with open(INPUT_FILE_NAME, "r") as input_file:
        for each_line in input_file:
            clean_line = each_line.strip()
            if not clean_line:
                continue  # this will skip blank lines
            raw_parts = each_line.split(":")  # Each line has a colon

            line_label = raw_parts[0].strip()  # label definition before the colon
            if len(raw_parts) > 1:
                line_data = raw_parts[1].strip()  # Property detail after the colon

            if line_label.startswith("Monkey"):
                current_monkey_number = int(line_label[6:])
                current_monkey_details = dict()  # Create en empty dict
                if verbose_output:
                    print(f"Found Monkey: {current_monkey_number}")

            elif line_label == "Starting items":
                item_parts = line_data.split(",")
                initial_vals = [int(start_worry) for start_worry in item_parts]
                current_monkey_details["items"] = initial_vals
                if verbose_output:
                    print(f"Initial: {initial_vals}")

            elif line_label == "Operation":
                assert line_data.startswith("new = "), "Unexpected operation definition"
                current_monkey_details["operation"] = line_data[6:].split(" ")
                if verbose_output:
                    print(f"Operation: {current_monkey_details['operation']}")

            elif line_label == "Test":
                assert line_data.startswith("divisible by"), "Unexpected Test"
                # "divisble by" has 12 characters
                current_monkey_details["divisor"] = int(line_data[12:])
                if verbose_output:
                    print(f"Test with divisor: {current_monkey_details['divisor']}")

            elif line_label == "If true":
                assert line_data.startswith("throw to monkey "), "Unexpected action"
                # "throw to monkey " has 16 characters
                current_monkey_details["target_if_true"] = int(line_data[16:])
                if verbose_output:
                    print(f"If  true: {current_monkey_details['target_if_true']}")

            elif line_label == "If false":
                assert line_data.startswith("throw to monkey "), "Unexpected action"
                # "throw to monkey " has 16 characters
                current_monkey_details["target_if_false"] = int(line_data[16:])
                monkey_stats[current_monkey_number] = current_monkey_details
                if verbose_output:
                    print(f"If false: {current_monkey_details['target_if_false']}")

            else:
                assert line_label == "Unexpected", f"Unexpected label{line_label}"

    return monkey_stats


monkey_data = read_monkey_data(verbose_output=True)


print(f"Result is: {monkey_data}")
