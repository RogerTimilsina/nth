"""coffee machine code project"""
"""makes 3 types of coffee: espresso, latte, cappuccino"""
"""tracks resources and money; shows report; checks resources; processes coins; checks if transaction is successful; 
    makes coffee"""
"""coin operated: quarters, dimes, nickels, pennies"""

logo = r"""
__        _______ _     ____ ___  __  __ _____   _____ ___
\ \      / / ____| |   / ___/ _ \|  \/  | ____| |_   _/ _ \
 \ \ /\ / /|  _| | |  | |  | | | | |\/| |  _|     | || | | |
  \ V  V / | |___| |__| |__| |_| | |  | | |___    | || |_| |
   \_/\_/  |_____|_____\____\___/|_|  |_|_____|   |_| \___/

  ____ ___  _____ _____ _____ _____
 / ___/ _ \|  ___|  ___| ____| ____|
| |  | | | | |_  | |_  |  _| |  _|
| |__| |_| |  _| |  _| | |___| |___
 \____\___/|_|   |_|   |_____|_____|

 __  __    _    ____ _   _ ___ _   _ _____
|  \/  |  / \  / ___| | | |_ _| \ | | ____|
| |\/| | / _ \| |   | |_| || ||  \| |  _|
| |  | |/ ___ \ |___|  _  || || |\  | |___
|_|  |_/_/   \_\____|_| |_|___|_| \_|_____|
"""


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    'milk': 200,
    'coffee': 100
}


def is_resources_enough(order_ingredient):
    """Returns True when order can be made"""
    for item in order_ingredient:
        if resources[item] < order_ingredient[item]:
            print(f"Sorry, there is not enough {item}")
            return False
    return True


def make_payment():
    global profit
    print('cost: $', drink['cost'])
    cash = int(input("Insert your money. $"))
    if cash >= drink['cost']:
        change = cash - drink['cost']
        if change > 0:
            print("Keep your change : $", change)
            profit += drink['cost']
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False


def make_coffee():
    for item in drink['ingredients']:
        resources[item] -= drink['ingredients'][item]
    return f"Here is your {choice} ☕. enjoy."


print(logo)
is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        is_on = False
        print('Coffee machine is turned off.')
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resources_enough(drink['ingredients']):  # if is_resources_enough == True
            if make_payment():
                print(make_coffee())
