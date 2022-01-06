import random

print("Welcome to Rock, Paper, Scissors game")
user_choice = int(input("What do you choose?\nType 1 for Rock, 2 for Paper or 3 for Scissors: "))
if user_choice >= 4 or user_choice < 1:
    print("You typed an invalid number, you lose!")
else:
    computer_choice = random.randint(1, 3)
    print('You chose: ', user_choice)
    print("Computer chose:", computer_choice)

    if user_choice == 1 and computer_choice == 3:
        print("You win!")
    elif computer_choice == 1 and user_choice == 3:
        print("You lose!")
    elif computer_choice > user_choice:
        print("You lose!")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw!")
