import random

def get_computer_choice():
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    return computer_choice

def get_user_choice():
    user_choice = input("Pick rock, paper or scissors: ")
    return user_choice