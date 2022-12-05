""" Advent of code 2022 - Puzzle 02

    https://adventofcode.com/2022/day/2

    John Tocher     
    Solution to puzzle 02 part 1
"""

INPUT_FILE_NAME = "puzzle_02_input.txt"

this_score = 0      # We will re-use this variable for each game
running_score = 0   # This will store our game total as per the rules

with open(INPUT_FILE_NAME, "r") as input_file:
    for each_line in input_file:
        clean_line = each_line.strip()  # This removes any whitepace from both ends,but not the middle
        line_parts = clean_line.split(" ")  # Create a list of items that were originally separated by spaces
        opponent_choice = line_parts[0]     # The opponents choice is the first item
        player_response = line_parts[1]     # Recommendation is the second item
        print(f"Opponent: {opponent_choice} You: {player_response}")
        this_score = 0
        if opponent_choice == "A": # Opponent chooses Rock
            
            if player_response == "X":  # Player chooses rock
                this_score = 1 + 3      # draw
            if player_response == "Y":  # Player chooses Paper
                this_score = 2 + 6      # draw
            if player_response == "Z":  # Player chooses Scissors
                this_score = 3 + 0      # loss
        
        if opponent_choice == "B": # Opponent chooses paper
            
            if player_response == "X":  # Player chooses Rock
                this_score = 1 + 0      # loss
            if player_response == "Y":  # Player chooses Paper
                this_score = 2 + 3      # draw
            if player_response == "Z":  # Player chooses Scissors
                this_score = 3 + 6      # win
        
        if opponent_choice == "C": # Opponent chooses scissors
            
            if player_response == "X":  # Player chooses Rock
                this_score = 1 + 6      # win
            if player_response == "Y":  # Player chooses Paper
                this_score = 2 + 0      # loss
            if player_response == "Z":  # Player chooses Scissors
                this_score = 3 + 3      # draw

        running_score = running_score + this_score
        
print(f"The total score was {running_score}")
