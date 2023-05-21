import random
rock="Rock"
papper="Papper"
scissors="Scissors"

player_move=input("Choose [r]ock, [p]apper, [s]cissorg: ")

if player_move=="r":
    player_move = rock

elif player_move=="p":
    player_move = papper

elif player_move=="s":
    player_move = scissors
else:
    print("İnvalid input. Try again...")
    exit()

print(f"Your Move:{player_move}")
computer_move=random.randint(1,3)
if computer_move==1:
    computer_move=rock

if computer_move==2:
    computer_move=papper

if computer_move==3:
    computer_move=scissors
print(f"Compuer move:{computer_move}")

if (player_move == rock and computer_move == scissors)or \
    (player_move == scissors and computer_move == papper)or \
    (player_move==papper and computer_move==rock):
    print("You Win!")
elif player_move==computer_move:
    print("DRAW")

else:
    print("You Lose!")


