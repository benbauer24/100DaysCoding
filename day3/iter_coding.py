print("This is the code exercise for day 3")
print("\n")

print("Note: ICE stands for Interative Coding Exercise")
print("\n\n")

#  ICE 1 - Odd or even
print("ICE 1 - Data types\n==============================")

# Writing a function check if a number is odd or even
def odd_or_even(number):
    """ 
    Description: A function that check if a number is odd or even
    
    Input: 
          number: Any integer
    
    Output: The number property (odd or even)
    """

    #Verify if the number is odd or even
    if number % 2 == 0:
        num_odd_or_even = "even"
    else:
        num_odd_or_even = "odd"

    #return the output
    return num_odd_or_even

# Prompt the user to enter an integer
print("Welcome to the ODD or EVEN checker!")
number = int(input("Which number do you want to check? \n"))

# Verify if the number is odd or even
num_status = odd_or_even(number)

# Print the number property (odd or even)
print(f"This is an {num_status} number.")

print("\n\n")

#  ICE 2 - BMI 2.0
print("ICE 2 - BMI 2.0\n==============================")

# Writing a function to calculate calculate and inteprete BMI value
def bmi_interpretor(weight, height):
    """ 
    Description: A function that calculates and interprete the Body Mass Index (BMI) from a user's weight and height
    
    Inputs:
          weight: weight of the user in kg
          height: height of the user in m
    
    Outputs: The Body Mass Index (BMI) interpretation

    """
    #Calculate the BMI
    bmi = round((weight / height**2), 0)

    #Interprete the BMI
    if bmi < 18.5:
        bmi_interpretation = "are underweight"
    elif bmi < 25:
        bmi_interpretation = "have a normal weight"
    elif bmi < 30:
        bmi_interpretation = "are slightly overweight"
    elif bmi < 35:
        bmi_interpretation = "are obese"
    else:
        bmi_interpretation = "are clinically obese"

    #Return the results
    return bmi, bmi_interpretation

# Prompt the user to enter weight (in kg) and height (in m)
print("Welcome to the BMI 2.0 interpretor!")
weight = float(input("enter your weight in kg: \n"))
height = float(input("enter your height in m: \n"))

#Calculate, interprete and print the BMI's results
bmi_value, bmi_interpretation = bmi_interpretor(weight, height)

print(f"Your BMI is {bmi_value:.0f}, you {bmi_interpretation}.")

print("\n\n")

#  ICE 3 - Pizza order
print("ICE 3 - Pizza order\n==============================")

# Writing a function to calculate the total amount of a pizza bill
def bill_amount(size, add_pepperoni, extra_cheese):
    """ 
    Description: A function that calculates the total amount of a pizza bill based on size and options
    
    Inputs:
          size: size of the pizza (S, M or L)
          add_pepperoni: option to add pepperoni (Y or N)
          extra_cheese: option to add extra cheese (Y or N)
    
    Outputs: The total amount of the bill
    """
    #Declare global constant variables
    global SMALL_PIZZA, MEDIUM_PIZZA, LARGE_PIZZA, PEPPERONI_SMALL_PIZZA, PEPPERONI_MEDIUM_LARGE_PIZZA, EXTRA_CHEESE

    #Calculate the final price
    final_price = 0
    if size == "S":
        final_price += SMALL_PIZZA
        if add_pepperoni == "Y":
            final_price += PEPPERONI_SMALL_PIZZA
    elif size == "M":
        final_price += MEDIUM_PIZZA
        if add_pepperoni == "Y":
            final_price += PEPPERONI_MEDIUM_LARGE_PIZZA
    else:
        final_price += LARGE_PIZZA
        if add_pepperoni == "Y":
            final_price += PEPPERONI_MEDIUM_LARGE_PIZZA

    if extra_cheese == "Y":
        final_price += EXTRA_CHEESE

    #return the outputs
    return final_price

#Variables declaration
SMALL_PIZZA = 15
MEDIUM_PIZZA = 20
LARGE_PIZZA = 25
PEPPERONI_SMALL_PIZZA = 2
PEPPERONI_MEDIUM_LARGE_PIZZA = 3
EXTRA_CHEESE = 1

# Prompt the user to enter his choice and options
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L? \n")
add_pepperoni = input("Do you want pepperoni? Y or N? \n")
extra_cheese = input("Do you want extra cheese? Y or N? \n")

#Calculate final price
total_amount = bill_amount(size, add_pepperoni, extra_cheese)

print(f"Your final bill is: ${total_amount}.")

print("\n\n")

#  ICE 4 - Love calculator
print("ICE 4 - Love calculator\n==============================")

# Writing a function to count the number of time a letter occurs in a name
def count_letter(name, letter):
    """ 
    Description: A function that counts the number of time a letter occurs in a name
    
    Inputs:
          name: The name to count letter occurence in
          letter: Letter that occurences should be counted

    Outputs: Number of occurences of letter in name
    """
    # Count occurences of letter in the name
    num_occ = name.lower().count(letter)

    #return the outputs
    return num_occ

#Write a function that combines two digits to form a score number
def combine_digits(digit1, digit2):
    """ 
    Description: A function that combines two digits to form a score number
    
    Inputs:
          digit1: First digit
          digit2: Second digit

    Outputs: Two digits number
    """
    # Form number from two digits
    score = int(str(digit1) + str(digit2))

    #return the outputs
    return score

#Write a function that prints a message based on score value
def print_message(score):
    """ 
    Description: A function that prints a message based on score value
    
    Inputs:
          score: Score value

    Outputs: The message related to score value
    """
    if score < 10 or score > 90:
        print(f"Your score is {score}, you go together like coke and mentos.")

    elif score > 40 and score < 50:
        print(f"Your score is {score}, you are alright together.")
    else:
        print(f"Your score is {score}.")

#Contant variables declaration
CHECK_STRING1 = "true"
CHECK_STRING2 = "love"

# Prompt the user to enter the names to check
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

#Calculate the number of occurences of each letter of TRUE in the first name
occ_True_Name_1 = [count_letter(name1, letter) for letter in CHECK_STRING1]

#Calculate the number of occurences of each letter of TRUE in the second name
occ_True_Name_2 = [count_letter(name2, letter) for letter in CHECK_STRING1]

#Calculate the number of occurences of each letter of LOVE in the first name
occ_Love_Name_1 = [count_letter(name1, letter) for letter in CHECK_STRING2]

#Calculate the number of occurences of each letter of LOVE in the second name
occ_Love_Name_2 = [count_letter(name2, letter) for letter in CHECK_STRING2]

#Calculate the score digits
score_dig1 = sum(occ_True_Name_1) + sum(occ_True_Name_2)
score_dig2 = sum(occ_Love_Name_1) + sum(occ_Love_Name_2)

# Calculate the love score and print message
love_score = combine_digits(score_dig1, score_dig2)
print_message(love_score)

print("\n\n")