import time


def clear_screen():
    clear = "\n" * 100
    print(clear)


def percent_of_num():
    print("You chose option #1 - What is x % of y?\n")
    x = float(input("What is the value of x?: "))
    y = float(input("What is the value of y?: "))
    answer = f"\n{x} is {(x * y) / 100}% of {y}\n"
    print(answer)
    another_calc()


def num_percent_of_num():
    print("You chose option #2 - x is what % of y?\n")
    x = float(input("What is the value of x?: "))
    y = float(input("What is the value of y?: "))
    answer = f"\n{x} is {(x * 100) / y}% of {y}"
    print(answer)
    another_calc()


def percent_num_to_num():
    print("You chose option #3 - What is the % increase/decrease from x to y?\n")
    x = float(input("What is the value of x?: "))
    y = float(input("What is the value of y?: "))
    if x > y:
        answer = f"\nThere is a -{((x - y) / x) * 100}% difference between {x} and {y}"
    else:
        answer = f"\nThere is a +{((y - x) / x) * 100}% difference between {x} and {y}"
    print(answer)
    another_calc()


def another_calc():
    response = input("\nWould you like to perform another calculation? (Y/N): ")
    if response == "Y" or response == "y":
        clear_screen()
        main()
    elif response == "N" or response == "n":
        clear_screen()
        print("Thanks for using the Percentage Calculator!")
    else:
        clear_screen()
        print("Choose a valid answer!\n")
        time.sleep(2)
        clear_screen()
        another_calc()


def main():
    print("Types of calculations:\n")
    print("1. What is x % of y?\n"
          "2. x is what % of y?\n"
          "3. What is the % increase/decrease from x to y?\n")

    choice = input("Select a calculation from 1-3: ")
    if choice == "1":
        clear_screen()
        percent_of_num()
    elif choice == "2":
        clear_screen()
        num_percent_of_num()
    elif choice == "3":
        clear_screen()
        percent_num_to_num()
    else:
        clear_screen()
        print("Choose a valid answer!\n")
        time.sleep(2)
        clear_screen()
        main()


print("Welcome to the Percentage Calculator!\n")
main()
