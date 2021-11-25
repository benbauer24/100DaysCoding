print("This is the code exercise for day 2")
print("\n")

print("Note: ICE stands for Interative Coding Exercise")
print("\n\n")

#  ICE 1 - Data types
print("ICE 1 - Data types\n==============================")

# Writing a function to sum the digits in a string number. The function can sum digits in any integer
def sum_digits_number(number):
    """ 
    Description: A function that sums the digits in a string number
    
    Input: 
          number: Any integer in string format
    
    Output: The sum of all the digits that form the input integer
    """

    #create a list of all digits that compose the number, with each digit converted to integer format
    num_list = [int(digit) for digit in input_number]

    #sum all the digit in the list
    digits_sum = sum(num_list)

    #return the output
    return digits_sum

# Prompt the user to enter an integer
print("Welcome to the Data types program!")
input_number = input("Type a two digit number: ")

#print the type of the input number
print(type(input_number))

print(sum_digits_number(input_number))

print("\n\n")

#  ICE 2 - BMI Calculator
print("ICE 2 - BMI Calculator\n==============================")

# Writing a function to calculate the Body Mass Index (BMI) from a user's weight and height
def bmi_calculator(weight, height):
    """ 
    Description: A function that calculates the Body Mass Index (BMI) from a user's weight and height
    
    Inputs:
          weight: weight of the user in kg
          height: height of the user in m
    
    Outputs: The Body Mass Index (BMI)

    """

    #Calculate the BMI
    BMI = round(weight / height**2)

    #return the output
    print(f"You BMI is {BMI}")


# Prompt the user to enter weight (in kg) and height (in m)
print("Welcome to the BMI Calculator!")
weight = float(input("enter your weight in kg: \n"))
height = float(input("enter your height in m: \n"))

#Calculate the BMI
bmi_calculator()

print("\n\n")

#  ICE 3 - Life on weeks
print("ICE 3 - Life on weeks\n==============================")

# Writing a function to calculate the Body Mass Index (BMI) from a user's weight and height
def life_remaining(age):
    """ 
    Description: A function that calculates number of weeks, months and days remaining until 90, based of user's age
    
    Inputs:
          age: User's current age
    
    Outputs: The number of weeks, months and days remaining until 90, based of user's age
    """
    #Declare global constant variable
    global MAX_YEAR

    #Calculate the number of weeks remaining
    num_weeks = (MAX_YEAR - age) * 52

    #Calculate the number of months remaining
    num_months = (MAX_YEAR - age) * 12

    #Calculate the number of days remaining
    num_days = (MAX_YEAR - age) * 365

    #return the outputs
    return num_days, num_months, num_weeks

#Variables declaration
MAX_YEAR = 90

# Prompt the user to enter his age
print("Welcome to the Life in weeks program!")
age = int(input("What is your current age?\n"))

#Calculate the number of days, months and weeks remaining
num_days, num_months, num_weeks = life_remaining(age)

print(f"You have {num_days} days, {num_weeks} weeks, and {num_months} months left")

print("\n\n")