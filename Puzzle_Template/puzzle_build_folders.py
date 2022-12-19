""" This file generates the base files for a particulr puzzle

    It does so by copying the four files in the template directory, 
    and then doing a search and replace on 'nn' for the puzzle number
"""

PUZZLE_TO_GENERATE = 12

TEMPLATE_FILES = [
    "puzzle_nn_input.txt",
    "puzzle_nn_notes.md",
    "puzzle_nn-part_1_jmt.py",
    "puzzle_nn-part_2_jmt.py",
]

from pathlib import Path

puzzle_num_1 = f"{PUZZLE_TO_GENERATE}"
puzzle_num_2 = f"{PUZZLE_TO_GENERATE:02}"

this_folder = Path(__file__).parent

target_folder = this_folder.parent / f"Puzzle_{puzzle_num_2}"
print(f"Top level folder is : {this_folder}")
print(f"   Target folder is : {target_folder}")

if not target_folder.exists():
    target_folder.mkdir(parents=False, exist_ok=False)
    print(f"Created folder: {target_folder}")
    # Create the folder if it doesn't exist, dont create parents

for template_file in TEMPLATE_FILES:
    input_filename = this_folder / template_file
    output_filename = target_folder / template_file.replace("nn", f"{puzzle_num_2}")

    with open(output_filename, "x") as output_file:
        print(f"Output is {output_filename}")
        with open(input_filename, "r") as input_file:
            print(f" Input is {output_filename}")
            for input_line in input_file:
                output_line = input_line.replace("nn", f"{puzzle_num_2}")
                output_line = output_line.replace("/day/n", f"/day/{puzzle_num_1}")
                output_file.write(f"{output_line.rstrip()}\n")

print("All done")
