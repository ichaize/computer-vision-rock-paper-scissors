import random

def get_computer_choice():
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    return computer_choice

def get_user_choice():
    user_choice = input("Pick rock, paper or scissors: ")
    return user_choice

computer_choice = get_computer_choice()
user_choice = get_user_choice()

def get_winner(computer_choice, user_choice):
    if computer_choice == user_choice:
        print("It is a tie!")
    elif computer_choice == "Rock":
        if user_choice == "Paper":
            print("You won!")
        else:
            print("You lost")
    elif computer_choice == "Paper":
        if user_choice == "Scissors":
            print("You won!")
        else:
            print("You lost")
    elif computer_choice == "Scissors":
        if user_choice == "Rock":
            print("You won!")
        else:
            print("You lost")


    