import random

options = ["stone", "paper", "scissor"]

WINNING_SCORE = 10
LOSSING_SCORE = 0
DRAW_SCORE = 5

scores = [] # [(Player 1, 10, Player 2, 0), ]

run = "yes"

# Enter Player 1 Name
# Enter Player 2 Name

while run == "yes":
    player_1 = random.choice(options)
    player_2 = random.choice(options)

    if player_1 == player_2:
        print(f"...Game Draw.... Player 1: {player_1} and Player 2: {player_2}")
        scores.append(("Player 1", DRAW_SCORE, "Player 2", DRAW_SCORE))
    elif player_1 == "stone" and player_2 == "scissor":
        print(f"... Player 1 Wins !!!... Player 1: {player_1} and Player 2: {player_2}")
        scores.append(("Player 1", WINNING_SCORE, "Player 2", LOSSING_SCORE))
    elif player_1 == "paper" and player_2 == "stone":
        print(f".. Player 1 Wins !!!.... Player 1: {player_1} and Player 2: {player_2}")
        scores.append(("Player 1", WINNING_SCORE, "Player 2", LOSSING_SCORE))
    elif player_1 == "scissor" and player_2 == "paper":
        print(f".. Player 1 Wins !!!.... Player 1: {player_1} and Player 2: {player_2}")
        scores.append(("Player 1", WINNING_SCORE, "Player 2", LOSSING_SCORE))
    else:
        scores.append(("Player 2", WINNING_SCORE, "Player 1", LOSSING_SCORE))
        print(f".. Player 2 Wins !!!.... Player 2: {player_2} and Player 1: {player_1}")

    run = input("Would you like to continue the game yes/no: ")

for game_score in scores:
    print(game_score)
