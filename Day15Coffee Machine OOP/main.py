from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from logo import logo
menu = Menu()
menu_item = MenuItem
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True
print(logo)
while is_on:

    print("--- Coffee Machine ---")
    choice = input("Which coffee would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        is_on = False
    elif choice == "latte" or choice == "espresso" or choice == "cappuccino":
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
    else:
        print("Please enter a valid option.\n")