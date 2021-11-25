print("This is the code exercise for day 1")
print("\n")

print("Note: ICE stands for Interative Coding Exercise")
print("\n\n")

#  ICE 1 - Printing Printing to the console
print("1 - Printing to the console\n==============================")
print("Hello World")
print("\n\n")

#  ICE 2 - Printing

# Simple printing exercise
print("2 - ICE - Printing\n==============================")
print(
    "Day 1 - Python Print Function\nThe function is declared like this:\nprint('what to print')"
)
print("\n\n")

#  ICE 3 - Debbuging

#Debug a code to run without error
print("3 - ICE - Debbuging\n==============================")
print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")
print("\n\n")

# ICE 4 - Input Function
print("4 - ICE - Input Function\n==============================")

# Writing a function calculate length of a username
def username_print(username):
    """ 
    Description: A function that receives a name and calculates the number of characters that the name contains
    
    Input: 
          name: User's name
    
    Output: The number of characters the name contains
    """
    #Calculate the number of characters in the name
    num_characters = len(username)

    #Return the results
    return num_characters

# Prompt the user to enter his name
username = input("What is your name?")

#Calculate the number of characters in the name
username_print(username)

#Print the length of the name
print(f"The name's length is: {username}")

print("\n\n")

# ICE 5 - Variables
print("5 - Variables\n==============================")

# Prompt the user to enter two variables
print("Imputing variables")
a = input("a: ")
b = input("b: ")
print("\n")

# Invert the entered variables
(a, b) = (b, a)

# Print the result
print("Reverted variables")
print(f"a: {a}")
print(f"b: {b}")
print("\n\n")
