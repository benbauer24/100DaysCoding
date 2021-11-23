#Final project for day 2

# FINAL PROJECT
print("Day 2 - Final project\n===============================\n")

#Functions
def tip_calculator(bill_amount, tips, num_person):
    """ 
    Description: Function that calculate the amount of bill for each person

    Inputs:
        bill_amount: total amount of the bill
        tips: Percentage of tips that the user want to pay
        num_person: Number of persons to split the bill

    Outputs: The amount of bill for each person
    """

    #Calculate the total amount including tip
    total_amount = bill_amount * (1+tips/100)

    # Calculate the amount per person
    amount_per_person = total_amount/num_person

    #return the output
    return amount_per_person

#1. Creating a greeting for the program.
print("Welcome to the Tip Calculator program")
print("\n")

#2. Asking the user for the total amount of the bill.
bill_amount = float(input("What was the total bill?\n"))
print("\n")

#3. Asking the user for the percentage of tip
tips = int(input("What percentage of tip would you like to give? 10, 12, or 15?\n"))
print("\n")


#3. Asking the user for the nhumber of people to split the bill
num_person = int(input("How many people to split the bill?\n"))
print("\n")

#4. Calculate the final amount for each person.
amount_per_person = tip_calculator(bill_amount, tips, num_person)

print(f"Each person should pay {amount_per_person:.2f}")