# stone, paper, scissor game

import random

game = {
         1 : "rock" ,
         0 : "paper",
        -1 : "scissor"
        }

print(" 1 : for rock ")
print(" 0 : for paper ")
print(" -1 : for scissor ")

computer = random.choice([-1,0,1])
player_2 = int(input("Enter your choice : "))

print(f"Computer chose {game[computer]}")
print(f"Player_2 chose {game[player_2]}")

if computer == 0 and player_2 == 1 or computer == 1 and player_2 == -1 or computer == -1 and player_2 == 0 :
    print("Computer wins")
elif player_2 == 0 and computer == 1 or player_2 == 1 and computer == -1 or player_2 == -1 and computer == 0 :
    print("Player_2 wins")  
else :
    print("its a draw")