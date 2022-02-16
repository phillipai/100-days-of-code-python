import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


choice = (input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n0/1/2:"))
computers_choice = random.randint(0,2)

if not choice.isdigit():
  print("You've entered an invalid value, try again and choose a number between 0-2.")
else:
  choice = int(choice)
  if choice > 2:
    print("You've entered an invalid number, try again and choose a number between 0-2.")
  elif choice == 0 or choice == 1 or choice == 2:
    if choice == 0:
      print(f"You chose: Rock {rock}")
    elif choice == 1:
      print(f"You chose: Paper {paper}")
    elif choice == 2:
      print(f"You chose: Scissors {scissors}")

    if computers_choice == 0:
      print(f"The computer chose: Rock {rock}")
      if choice == 2:
        print("You lose, Rock wins against scissors.")
      elif choice == 0:
        print("It's a draw!")
      else:
        print("You win!")

    elif computers_choice == 1:
      print(f"The computer chose: Paper {paper}")
      if choice == 0:
        print("You lose, Paper wins against rock.")
      elif choice == 0:
        print("It's a draw!")
      else:
        print("You win!")

    elif computers_choice == 2:
      print(f"The computer chose: Scissors {scissors}")
      if choice == 1:
        print("You lose, Scissors win against paper.")
      elif choice == 2:
        print("It's a draw!")
      else:
        print("You win!")
