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

def set_player_score(games_result):
    for name, score in games_result.items():
        player_scores = scores.get(name, [])
        player_scores.append(score)
        scores[name] = player_scores

while run == "yes":

    player_1 = random.choice(options)
    player_2 = random.choice(options)

    if player_1 == player_2:
        print(f"...Game Draw.... {player_1_name}: {player_1} and {player_2_name}: {player_2}")

        set_player_score({player_1_name : DRAW_SCORE, player_2_name:  DRAW_SCORE})
        
    elif player_1 == "stone" and player_2 == "scissor":
        print(f"... {player_1_name} Wins !!!... {player_1_name}: {player_1} and {player_2_name}: {player_2}")
        
        set_player_score({player_1_name : WINNING_SCORE, player_2_name:  LOSSING_SCORE})

    elif player_1 == "paper" and player_2 == "stone":
        print(f"... {player_1_name} Wins !!!... {player_1_name}: {player_1} and {player_2_name}: {player_2}")
        
        set_player_score({player_1_name : WINNING_SCORE, player_2_name:  LOSSING_SCORE})

    elif player_1 == "scissor" and player_2 == "paper":
        print(f"... {player_1_name} Wins !!!... {player_1_name}: {player_1} and {player_2_name}: {player_2}")
        #set_player_score({player_1_name = WINNING_SCORE, player_2_name = LOSSING_SCORE})
        set_player_score({player_1_name : WINNING_SCORE, player_2_name:  LOSSING_SCORE})

    else:
        print(f"... {player_2_name} Wins !!!... {player_2_name}: {player_2} and {player_1_name}: {player_1}")
        
        set_player_score({player_1_name : LOSSING_SCORE, player_2_name:  WINNING_SCORE})

    run = input("Would you like to continue the game yes/no: ")

for k, v in scores.items():
    print(f"{k} games scores are: {v}")
