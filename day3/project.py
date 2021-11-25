#Final project for day 3

# FINAL PROJECT
print("Day 3 - Final project\n===============================\n")

#Functions
def random_generator(choice):
    """ 
    Description: Function that take a tuple of choices, then generatea a random index between 0 and the last index of the tuple. The user only pass the step if his choice has the same index as the random index

    Inputs:
        *args: any number of positional arguments

    Outputs: a random index between 0 and the last index of the input.
    """

    # Generation the random index
    import random
    random_index = random.randint(0, (len(choice)-1))

    return random_index


#1 Constant choice for each step
CROSS_ROAD_CHOICES = ("left", "right")
LAKE_CROSS_CHOICES = ("wait", "swim")
DOOR_CHOICES = ("red", "yellow", "blue")

#2. Creating a greeting for the program.
print("Welcome to the Treasure Island!\nYour mission is to find the treasure!!\nGood Luck!!!!\n")

#3. Check user anwser for the cross road
user_direction = input("You are at a cross road. Where do you want to go? Type 'left' or 'right.'\n").lower()
print("\n")

success_index = random_generator(CROSS_ROAD_CHOICES)
good_direction = CROSS_ROAD_CHOICES[success_index]

if user_direction == good_direction:
    pass
else:
    print("You are lost!! GAME OVER!")
    quit()

#4. Check user anwser for the lake cross
lake_cross = input("You came to a lake. The is an island in the middle of the lake. Type 'wait'to wait for a boat or type 'swim' to swim accross.\n").lower()
print("\n")

success_index = random_generator(LAKE_CROSS_CHOICES)
good_lake_cross = LAKE_CROSS_CHOICES[success_index]

if lake_cross == good_lake_cross:
    pass
else:
    print("You failed to cross the lake!! GAME OVER!")
    quit()

#5. Check user anwser for the door selection
door_choice = input("You arrive at the island unharmed. There is a house with three doors. One red, one yellow and one blue. Which colour do you choose?\n").lower()
print("\n")

success_index = random_generator(DOOR_CHOICES)
good_door = DOOR_CHOICES[success_index]

if door_choice == good_door:
    print("Congratulations, you found the treasure!!!")
else:
    print("You enter a room of beast! Game over!")
