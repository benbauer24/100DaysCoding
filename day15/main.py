"""
Programming a coffee machine

"""

from object_classes.coffee_objects import CoffeeMachine

Machine = CoffeeMachine()
coffee_str = ""
coffee_machine_on = True

while coffee_machine_on:
    coffees_in_menu = Machine.list_coffee_menu()
    print("==========Choice Screen ==============")
    user_choice = input("What would you like? \nOff\nReport\nAdd New Coffee\n" +
                        coffees_in_menu + "\nEnter your choice: ").capitalize()
    print()

    if user_choice == "Off":
        print("Coffee machine off for maintenance\n...   ...   ...")
        coffee_machine_on = False
        continue

    elif user_choice == "Report":
        Machine.show_report()
        continue

    elif user_choice == "Add new coffee":
        coffee_name = input("Enter the new coffee's Name: ").capitalize()
        Machine.create_new_coffee(coffee_name)
        print()
        continue

    elif not Machine.menu:
        print("We don't have any coffee in our menu at the moment. Please come back later!!\n")
        continue

    elif user_choice not in Machine.menu:
        print("Sorry, we don't offer this choice at the moment!! Please select a different option\n")

    else:
        user_coffee = Machine.menu[user_choice]
        water_in_machine = Machine.water
        milk_in_machine = Machine.milk
        coffee_in_machine = Machine.coffee
        enough_resource = user_coffee.check_if_enough_resource(water_in_machine, milk_in_machine, coffee_in_machine)

    if not enough_resource:
        continue

    else:
        quarter = float(input("Enter the number of quarter coins: "))
        dimes = float(input("Enter the number of dimes coins: "))
        nickles = float(input("Enter the number of nickles coins: "))
        pennies = float(input("Enter the number of pennies coins: "))

        user_inserted_money = quarter * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01

        if user_inserted_money < user_coffee.price:
            print(f"Sorry, That is not enough money for a coffee {user_choice}!! Money refunded!")

        else:
            user_refund = user_inserted_money - user_coffee.price
            Machine.money += user_coffee.price
            Machine.water -= user_coffee.water
            Machine.milk -= user_coffee.milk
            Machine.coffee -= user_coffee.coffee

            print(f"Thanks for your order, we are preparing you coffee.\n"
                  f"Your refund is ${round(user_refund,2)}\n...  ...\n...  ...\n\n")

            print(f"Your {user_choice} is ready! Enjoy!!\n\n ")
