"""
Adevnt of Code 2022, Day 2!
Alastair Cottier
December 2, 2022

"""

# Opponent Strategy: 
# A is Rock
# B is Paper 
# C is Scissors 

# Your Strategy: 
# X is Rock 
# Y is Paper
# Z is Scissors 

# Match Result Scoring: 
win = 6
draw = 3
loss = 0

# Shape Selected Scoring
rock = 1
paper = 2
scissors = 3

# Create Dictionary
scores = {
        "X": rock,
        "Y": paper,
        "Z": scissors,
        "A": rock,
        "B": paper,
        "C": scissors
        }

inp_file = open("advent_day_2.txt", "r")
lines = inp_file.readlines()
score = 0


for line in lines:
    line.strip()
    line.split()
    score += scores[line[2]]  # Add Shape Selected Score

    if scores[line[0]] == scores[line[2]]: # Draw
        score += draw

    if scores[line[2]] == rock and scores[line[0]] == scissors: # Rock beats Scissors Case, Win
        score += 6

    elif (scores[line[2]] - scores[line[0]]) == 1: # All other win cases
        score += 6

    else:  # You Lose 
        score += 0

print(score)
