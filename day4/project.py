#Final project for day 3

# FINAL PROJECT
print("Day 4 - Final project\n===============================\n")

#Functions
def random_selector():
    """ 
    Description: Function that randomly selects the computer choice from a dictionnary

    Inputs: None
        

    Outputs: a random computer choice from the options dictionnary.
    """
    global options

    # Generate the random key
    computer_choice = random.choice(list(options.keys()))

    return computer_choice


def winner_finder(user_choice, computer_choice):
    """ 
    Description: Function that takes user and computer choices and determine who wins the game

    Inputs: 
          user_choice: The choice of the user
          computer_choice: The choice of the computer
        
    Outputs: Game result.
    """
    if user_choice == computer_choice:
        print("Draw Game!! No one wins!🤝🤝🤝")
    elif user_choice == "scissors":
        if computer_choice == "paper":
            print("Congratulations, user WIN!!!! 👏👏👏")
        else:
            print("Game over, Computer wins!!🥴🥴🥴")
    elif user_choice == "paper":
        if computer_choice == "rock":
            print("Congratulations, user WIN!!!!👏👏👏")
        else:
            print("Game over, Computer wins!!🥴🥴🥴")
    elif user_choice == "rock":
        if computer_choice == "scissors":
            print("Congratulations, user WIN!!!!👏👏👏")
        else:
            print("Game over, Computer wins!!🥴🥴🥴")


# 1. Import modules and librairies
import random

# 2. Constant choice for each step
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# 3. Storing options into a dictionnary
options = {"rock": rock, "paper": paper, "scissors": scissors}

# 4. Prompt user to play
print("Welcome to the ROCK, PAPER, SCISSORS game!!!")
user_choice = input("Enter you choice! 'rock', 'paper', or 'scissors': \n").lower()
print("\n\n")

print(f"USER CHOICE: {user_choice}\n{options[user_choice]}")

# 5. let computer play
computer_choice = random_selector()
print(f"COMPUTER CHOICE: {computer_choice}\n{options[computer_choice]}")

# 6. Find the winner
winner_finder(user_choice, computer_choice)

