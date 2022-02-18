from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# List of drinks
espresso = MenuItem("espresso", 50, 0, 18, 1.5)
latte = MenuItem("latte", 200, 150, 24, 2.5)
cappuccino = MenuItem("cappuccino", 250, 100, 24, 3.0)

# For ordering drinks and checking if drink is available
menu = Menu()

# Printing report of all resources, checking if resources are sufficient, making coffee
coffee_maker = CoffeeMaker()

# Printing report and taking payment
money_machine = MoneyMachine()

on = True
while on:
    choice = input(f"What would you like? Choose between espresso, latte or cappuccino: ")
    if choice == 'off':
        print("Have a good one!")
        on = False
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        coffee_choice = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(espresso) and money_machine.make_payment(espresso.cost):
            coffee_maker.make_coffee(coffee_choice)
