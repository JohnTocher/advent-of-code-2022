""" Advent of code 2022 - Puzzle 11

    https://adventofcode.com/2022/day/11

    John Tocher
    Solution to puzzle 11 part 1
"""
1
INPUT_FILE_NAME = "puzzle_11_input.txt"


def monkey_inspection_result(worry_level, monkey_details, print_verbose=False):
    """Perfroms the inspection according to the rules"""

    initial_value = worry_level

    assert monkey_details["operation"][0] == "old", "Unexpected operation"
    operator = monkey_details["operation"][1]
    operand = monkey_details["operation"][2]

    if operator == "+":
        if operand == "old":
            final_value = initial_value + initial_value
        else:
            final_value = initial_value + int(operand)

    elif operator == "*":
        if operand == "old":
            final_value = initial_value * initial_value
        else:
            final_value = initial_value * int(operand)

    else:
        assert False, f"Unknown operator: {operator}"

    divisor = monkey_details["divisor"]
    assert divisor > 0, f"Unexpected divisor: {divisor}"

    bored_value = int(final_value / 3)

    if bored_value % divisor:  # have a remainder
        test_result = False
    else:
        test_result = True

    if test_result:
        target = monkey_details["target_if_true"]
    else:
        target = monkey_details["target_if_false"]

    if print_verbose:
        print(
            f"From {initial_value} to {final_value}, test:{test_result} div:{divisor} bored :{bored_value} thrown to {target}"
        )

    return (target, bored_value)


def print_monkey_data(all_data):
    """Prints the data as in the example"""

    for monkey_num, monkey_details in all_data.items():
        line_label = f"Monkey {monkey_num:02}"
        line_list = ", ".join([str(item) for item in monkey_details["items"]])
        line_insp = f"{monkey_details['inspections']}"
        print(f"{line_label} - {line_list.ljust(50)} Insp:{line_insp}")


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
                current_monkey_details["inspections"] = 0
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


group_data = read_monkey_data(verbose_output=False)

for round_count in range(1, 21):
    print(f"After round {round_count:02}")
    for monkey_num, monkey_data in group_data.items():
        # print(f"Round {round_count:02} Monkey {monkey_num:02}")
        inspection_count = monkey_data["inspections"]
        for each_item in monkey_data["items"]:
            inspection_count += 1
            target, worry_value = monkey_inspection_result(
                each_item, monkey_data, print_verbose=False
            )
            target_items = group_data[target]["items"]
            target_items.append(worry_value)
            group_data[target]["items"] = target_items

        group_data[monkey_num]["items"] = list()  # This monkey now empty handed
        group_data[monkey_num]["inspections"] = inspection_count

    print_monkey_data(group_data)

# Create an empty list to hold the numeric inspection counts
inspection_counts = list()
for _monkey_num, monkey_data in group_data.items():
    inspection_counts.append(monkey_data["inspections"])

inspection_counts.sort(reverse=True)  # Reverse to get biggest to smallest
monkey_business = inspection_counts[0] * inspection_counts[1]

print(f"Result is: {monkey_business}")
