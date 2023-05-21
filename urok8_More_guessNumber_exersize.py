import random
computer_number=random.randint(1,100)
while True:
    print(computer_number)
    player_input=input("Guess the number 1-100:")
    
    if not player_input.isdigit():
        print("plase input a number !")
        continue
    player_number=int(player_input)
    if player_number==computer_number:
        print("You guess it !!!")
        break
    elif player_number<computer_number:
        print("Number is HİGHER than you guess")
    
    elif player_number>computer_number:
        print("Number is LESS than you guess")