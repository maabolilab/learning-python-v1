import random

options = ["stone", "paper", "scissor"]

WINNING_SCORE = 10
LOSSING_SCORE = 0
DRAW_SCORE = 5

scores = {} # { "Player1" : [10, 0, 5], "Player2": [0, 10, 5]}

run = "yes"

player_1_name = input("Enter Player 1 name: ")
player_2_name = input("Enter Player 2 name: ")

print(f"Hello {player_1_name} and {player_2_name} in pur gaming zone.")

while run == "yes":

    player_1 = random.choice(options)
    player_2 = random.choice(options)

    if player_1 == player_2:
        print(f"...Game Draw.... {player_1_name}: {player_1} and {player_2_name}: {player_2}")
        player1_scores = scores.get(player_1_name, [])
        player2_scores = scores.get(player_2_name, [])

        player1_scores.append(DRAW_SCORE)
        player2_scores.append(DRAW_SCORE)

        scores[player_1_name] = player1_scores
        scores[player_2_name] = player2_scores

    elif player_1 == "stone" and player_2 == "scissor":
        print(f"... {player_1_name} Wins !!!... {player_1_name}: {player_1} and {player_2_name}: {player_2}")
        player1_scores = scores.get(player_1_name, [])
        player2_scores = scores.get(player_2_name, [])

        player1_scores.append(WINNING_SCORE)
        player2_scores.append(LOSSING_SCORE)

        scores[player_1_name] = player1_scores
        scores[player_2_name] = player2_scores

    elif player_1 == "paper" and player_2 == "stone":
        print(f"... {player_1_name} Wins !!!... {player_1_name}: {player_1} and {player_2_name}: {player_2}")
        player1_scores = scores.get(player_1_name, [])
        player2_scores = scores.get(player_2_name, [])

        player1_scores.append(WINNING_SCORE)
        player2_scores.append(LOSSING_SCORE)

        scores[player_1_name] = player1_scores
        scores[player_2_name] = player2_scores

    elif player_1 == "scissor" and player_2 == "paper":
        print(f"... {player_1_name} Wins !!!... {player_1_name}: {player_1} and {player_2_name}: {player_2}")
        
        player1_scores = scores.get(player_1_name, [])
        player2_scores = scores.get(player_2_name, [])

        player1_scores.append(WINNING_SCORE)
        player2_scores.append(LOSSING_SCORE)

        scores[player_1_name] = player1_scores
        scores[player_2_name] = player2_scores

    else:
        print(f"... {player_2_name} Wins !!!... {player_2_name}: {player_2} and {player_1_name}: {player_1}")
        player1_scores = scores.get(player_1_name, [])
        player2_scores = scores.get(player_2_name, [])

        player1_scores.append(LOSSING_SCORE)
        player2_scores.append(WINNING_SCORE)

        scores[player_1_name] = player1_scores
        scores[player_2_name] = player2_scores

    run = input("Would you like to continue the game yes/no: ")

for k, v in scores.items():
    print(f"{k} games scores are: {v}")
