""" Advent of code 2022 - Puzzle 07

    https://adventofcode.com/2022/day/7

    John Tocher
    Solution to puzzle 07 part 1
"""

INPUT_FILE_NAME = "puzzle_07_input.txt"
# INPUT_FILE_NAME = "puzzle_07_sample_input.txt"

folders = dict()
current_folder_data = dict()
current_dir = ""
line_num = 0


def find_parent_dir(base_dir):
    """Returns the parent directory assumeing they are separated by forward slashes"""

    assert base_dir != "/", "Can't find parent of root folder"

    last_slash = base_dir.rfind("/")
    parent_dir = base_dir[0:last_slash]

    if parent_dir:
        return parent_dir
    else:
        return "/"


def size_of_folder(folder_name):
    """recursively determines the size of the given folder"""

    total_size = folders[folder_name]["size"]

    sub_folders = folders[folder_name]["folders"]

    if sub_folders:
        for each_sub_folder in sub_folders:
            total_size += size_of_folder(each_sub_folder)

    return total_size


with open(INPUT_FILE_NAME, "r") as input_file:
    for each_line in input_file:
        clean_line = each_line.strip()
        line_num += 1
        # This removes any whitepace from both ends,but not the middle
        if clean_line.startswith("$"):
            known_cmd = False  # Doing some error checking
            # This is a user command, either cd or ls
            cmd_part = clean_line[2:]  # Remove the $ and the space after it

            if cmd_part[0:2] == "cd":
                new_dir = cmd_part[3:]
                if new_dir == "/":
                    current_dir = new_dir
                elif new_dir == "..":
                    current_dir = find_parent_dir(current_dir)
                else:
                    if current_dir == "/":
                        current_dir = f"/{new_dir}"
                    else:
                        current_dir = f"{current_dir}/{new_dir}"
                if current_dir not in folders:
                    # No entry for this folder, create it and set defaults
                    # Only necessary in case we never do an "ls" here
                    sub_folder_data = dict()
                    sub_folder_data["size"] = 0
                    sub_folder_data["folders"] = list()
                    folders[current_dir] = sub_folder_data

            else:  # This should be the "ls" command
                assert cmd_part[0:2] == "ls", f"Unexpected command: {cmd_part}"
                # Reset the size of files in this folder as we're about to re-calc
                sub_folder_data = dict()
                sub_folder_data["size"] = 0
                sub_folder_data["folders"] = list()
                current_folder_data = sub_folder_data

        else:  # Not a command, must be listing output

            if clean_line.startswith("dir"):
                # Telling us we have a subdirectory
                if current_dir == "/":
                    this_dir = f"/{clean_line[4:]}"
                else:
                    this_dir = f"{current_dir}/{clean_line[4:]}"
                new_folders = [
                    each_folder for each_folder in current_folder_data["folders"]
                ]
                new_folders.append(this_dir)
                current_folder_data["folders"] = new_folders

            else:
                # This ought to be a file size in the form NNNN FileName
                size_parts = clean_line.split(" ")
                size_value = int(size_parts[0])
                file_name = size_parts[1]
                current_folder_data["size"] = current_folder_data["size"] + size_value

            new_folder_data = dict()
            new_folder_data["size"] = current_folder_data["size"]
            new_folder_data["folders"] = current_folder_data["folders"]

            folders[current_dir] = new_folder_data

# Have read the folders into our dictionary, now get the result

total_under_limit = 0
for folder_name, folder_data in folders.items():
    this_size = size_of_folder(folder_name)
    if this_size <= 100000:
        total_under_limit += this_size

print(f"Total size of folders under limit is {total_under_limit}")
