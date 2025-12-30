import random

options = ["stone", "paper", "scissor"]

player_1 = random.choice(options)
player_2 = random.choice(options)

if player_1 == player_2:
    print(f"...Game Draw.... Player 1: {player_1} and Player 2: {player_2}")
elif player_1 == "stone" and player_2 == "scissor":
    print(f"... Player 1 Wins !!!... Player 1: {player_1} and Player 2: {player_2}")
elif player_1 == "paper" and player_2 == "stone":
    print(f".. Player 1 Wins !!!.... Player 1: {player_1} and Player 2: {player_2}")
elif player_1 == "scissor" and player_2 == "paper":
    print(f".. Player 1 Wins !!!.... Player 1: {player_1} and Player 2: {player_2}")
else:
    print(f".. Player 2 Wins !!!.... Player 2: {player_2} and Player 1: {player_1}")
