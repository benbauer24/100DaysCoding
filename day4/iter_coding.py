print("This is the code exercise for day 4")
print("\n")

print("Note: ICE stands for Interative Coding Exercise")
print("\n\n")

#  ICE 1 - Odd or even
print("ICE 1 - Head or tail\n==============================")

# Writing a function that randomly selects head or tail
def head_or_tail():
    """ 
    Description: A function that randomly selects head or tail

    Input: None

    Output: head or tail
    """

    # Generate a random number
    rand_num = random.randint(0, 1)

    if rand_num == 0:
        print("Tails")
    else:
        print("Heads")

import random

#Prompt the user to enter a seed
print("Welcome to the Heads or Tails program!")
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Randomly select head or Tail
head_or_tail()



print("\n\n")

#  ICE 2 - Banker Roulette
print("ICE 2 - Banker Roulette\n==============================")

# Writing a function to determine who is going to pay the bill
def banker_roulette(name_str):
    """ 
    Description: A function that determines who is going to pay the bill
    
    Inputs:
          name_str: a list of name
    
    Outputs: Name of the person who will pay the bill

    """
    # Determine the person who will pay the bill
    names = names_string.split(", ")

    ran_selector = random.randint(0, (len(names)-1))

    payer = names[ran_selector]

    return payer

#Prompt the user to enter a seed
print("Welcome to the Banker Roulette!")
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

#Prompt the user to enter the names
names_string = input("Give me everybody's names, separated by a comma: \n")

# Determine the person who will pay the bill
payer_name = banker_roulette(names_string)

print(f"{payer_name} is going to buy the meal today!")

print("\n\n")

#  ICE 3 - Treasure map
print("ICE 3 - Treasure map\n==============================")

# Writing a function to place the treasure ('X') at given location
def place_treasure(location):
    """ 
    Description: A function that places the treasure ('X') at given location
    
    Inputs:
          location: Position to place the treasure on the map
    
    Outputs: The map, with treasure at the specified location
    """
    global map, TREASURE
    # Determine the row and column
    col = int(location[0])-1
    row = int(location[1])-1

    # Place the treasure a specified location
    map[row][col] = TREASURE

    # Return the outputs
    print(f"{ROW_1}\n{ROW_2}\n{ROW_3}\n")

#Constant variables declaration
ROW_1 = ["😌", "😌", "😌"]
ROW_3 = ["😌", "😌", "😌"]
ROW_2 = ["😌", "😌", "😌"]

TREASURE = "💰"

#Create the map
map = [ROW_1, ROW_2, ROW_3]

print(f"{ROW_1}\n{ROW_2}\n{ROW_3}\n")

# Prompt the user to enter his chosen position on the map
print("Welcome to the Treasure map!")
position = input("Where do you want to put the treasure? \n")

#Place the treasure at the specified location
place_treasure(position)

print("\n\n")