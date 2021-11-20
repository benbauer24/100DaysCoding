"""
The file contains modules for the coffee machine

"""

# Define a class for the coffee machine


class CoffeeMachine:

    def __init__(self):
        self.water = 100
        self.milk = 100
        self.coffee = 100
        self.money = 0
        self.menu = {}

    def __str__(self):
        return f"This is a first class coffee machine"

    def show_report(self):
        print(" ==========Coffee Machine Report ===========")
        print(f"Water: {self.water}ml\nMilk: {self.milk}ml\nCoffee: {self.coffee}g\n"
              f"Money: ${self.money}\n")

    def create_new_coffee(self, name):
        new_coffee = Coffee(name)
        self.menu[name] = new_coffee

    def list_coffee_menu(self):
        coffee_list = []
        coffees_in_menu = self.menu.keys()
        [coffee_list.append(coffee) for coffee in coffees_in_menu]
        coffee_str = "\n".join(coffee_list)
        return coffee_str


# Define a class for the coffees
class Coffee:
    def __init__(self, name):
        self.name = name
        self.water = f"Enter water quantity for coffee {self.name} (in mL): "
        self.milk = f"Enter milk quantity for coffee {self.name} (in mL): "
        self.coffee = f"Enter coffee quantity for coffee {self.name} (in grams): "
        self.price = f"Enter price for coffee {self.name} (in $): "

    def __str__(self):
        return f"The is a {self.name} coffee. It contains {self.water} mL of water," \
               f"{self.milk} mL of milk and {self.coffee} grams of coffee. It cost" \
               f"${self.price}"

    def check_if_enough_resource(self, water, milk, coffee):
        enough_resource = True
        if self.water < water:
            print(f"Sorry, there is not enough water for your {self.name} coffee")
            enough_resource = False
        elif self.milk < milk:
            print(f"Sorry, there is not enough milk for your {self.name} coffee")
            enough_resource = False
        elif self.coffee < coffee:
            print(f"Sorry, there is not enough coffee for your {self.name} coffee")
            enough_resource = False

        return enough_resource


