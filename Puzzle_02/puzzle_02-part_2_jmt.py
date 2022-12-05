""" Advent of code 2022 - Puzzle 02

    https://adventofcode.com/2022/day/2

    John Tocher     
    Solution to puzzle 02 part 2
"""

INPUT_FILE_NAME = "puzzle_02_input.txt"

this_score = 0      # We will re-use this variable for each game
running_score = 0   # This will store our game total as per the rules

with open(INPUT_FILE_NAME, "r") as input_file:
    for each_line in input_file:
        clean_line = each_line.strip()  # This removes any whitepace from both ends,but not the middle
        line_parts = clean_line.split(" ")  # Create a list of items that were originally separated by spaces
        opponent_choice = line_parts[0]     # The opponents choice is the first item
        round_outcome = line_parts[1]     # Recommendation is the second item
        print(f"Opponent: {opponent_choice} Outcome: {round_outcome}")
        this_score = 0
        if opponent_choice == "A": # Opponent chooses Rock
            
            if round_outcome == "X":    # Need to lose
                this_score = 3 + 0      # scissors to lose
            if round_outcome == "Y":    # Need to draw
                this_score = 1 + 3      # rock to draw
            if round_outcome == "Z":    # Need to Win
                this_score = 2 + 6      # paper to win
        
        if opponent_choice == "B": # Opponent chooses paper
            
            if round_outcome == "X":    # Need to lose
                this_score = 1 + 0      # rock to lose
            if round_outcome == "Y":    # Need to draw
                this_score = 2 + 3      # paper to draw
            if round_outcome == "Z":    # Need to Win
                this_score = 3 + 6      # scissors to win
        
        if opponent_choice == "C": # Opponent chooses scissors
            
            if round_outcome == "X":    # Need to lose
                this_score = 2 + 0      # paper to lose
            if round_outcome == "Y":    # Need to draw
                this_score = 3 + 3      # scissors to draw
            if round_outcome == "Z":    # Need to Win
                this_score = 1 + 6      # rock to win

        running_score = running_score + this_score
        
print(f"The total score was {running_score}")
