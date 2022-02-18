MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = {
    "value": 0,
}


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money['value']}")


def check_resources(coffee_choice):
    enough = True
    if MENU[coffee_choice]['ingredients']['water'] > resources['water']:
        print(f"There isn't enough water for a {coffee_choice}.")
        enough = False
    if MENU[coffee_choice]['ingredients']['coffee'] > resources['coffee']:
        print(f"There isn't enough coffee for a {coffee_choice}.")
        enough = False
    if coffee_choice != 'espresso':
        if MENU[coffee_choice]['ingredients']['milk'] > resources['milk']:
            print(f"There isn't enough milk for a {coffee_choice}.")
            enough = False
    return enough


def process_coins(quarter, dime, nickle, penny):
    quarter *= 0.25
    dime *= 0.10
    nickle *= 0.05
    penny *= 0.01
    total = quarter + dime + nickle + penny
    return total


def deduct_resources(coffee_choice):
    resources['water'] -= MENU[coffee_choice]['ingredients']['water']
    resources['coffee'] -= MENU[coffee_choice]['ingredients']['coffee']
    if coffee_choice != 'espresso':
        resources['milk'] -= MENU[coffee_choice]['ingredients']['milk']


def coffee_machine():
    on = True
    while on:
        choice = input("What would you like? Type 'espresso', 'latte', 'cappuccino': ")
        if choice == 'report':
            report()
            coffee_machine()
        elif choice == 'off':
            print("Turning off.")
            on = False
        elif check_resources(choice):
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            if process_coins(quarters, dimes, nickles, pennies) == MENU[choice]['cost']:
                deduct_resources(choice)
                money['value'] += MENU[choice]['cost']
                print(f"Here is your {choice} ☕. Have a good one!")
            elif process_coins(quarters, dimes, nickles, pennies) > MENU[choice]['cost']:
                deduct_resources(choice)
                money['value'] += MENU[choice]['cost']
                change = process_coins(quarters, dimes, nickles, pennies) - MENU[choice]['cost']
                change = round(change, 2)
                print(f"Here is ${change} in change.")
                print(f"Here is your {choice} ☕. Have a good one!")
            else:
                print(f"Not enough money, ${(process_coins(quarters, dimes, nickles, pennies))} refunded.")


coffee_machine()
