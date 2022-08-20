# print('Automate the Boring Stuff Chapter 2')

#Chapter 2
#flow control example

#name = 'Mary'
#password = 'swordfish'
#
#if name == 'Mary':
#  print('Hello Mary')
#  if password == 'swordfish':
#    print('access granted')
#  else:
#    print('wrong password')

#name = 'Carol'
#age = 45
#if name == 'Alice':
# print('Hi, Alice.')
#elif age < 12:
# print('You are not Alice, kiddo.')
#elif age > 2000:
# print('Unlike you, Alice is not an undead, immortal vampire.')
#elif age > 100:
# print('You are not Alice, grannie.')


# Conditional loop while name is untrue
#name = ''
#while name != 'timmy':
# print('Please type your name.')
# name = input()
#print('Thank you!')


#Infinite loop with a break statement
#while True:
# print('Please type your name.')
# name = input()
# if name == 'your name':
#  break
#print('Thank you!')

#while True:
#  print('Who are you?')
#  name = input()
#  if name != 'Joe':
#    continue
#  print('Hello, Joe. What is the password? (It is a fish.)')
#  password = input()
#  if password == 'swordfish':
#    break
#print('Access granted.')

# Using a range for a loop (for loop)
#print('My name is')
#for i in range(5):
# print('Jimmy Five Times (' + str(i+1) + ')')

# Creating a range with loop (while loop)
# print('My name is')
# i = 0
# while i < 5:
#  print('Jimmy Five Times (' + str(i) + ')')
#  i = i + 1

# Carl Fredrich Gauss
# total = 0
# for num in range(10):
#   total = total + num
# print(total)

# range counting backwards with the step function
# for i in range(4, -1, -1):
#   print (i+1)

# Modules
# Random Module
# import random
# for i in range(10):
#   print(random.randint(1, 10))

# Using sys.exit()
# import sys

# while True:
#   print('Type exit to exit.')
#   response = input()
#   if response == 'exit':
#     sys.exit()
#   print('you typed ' + response + '.')

# Guess the number game
# import random
# secretNumber = random.randint(1,20)
# print('I am thinking of a number betwen 1 and 20.')

# for guessesTaken in range(1, 7):
#   print('take a guess')
#   guess = int(input())

#   if guess < secretNumber:
#     print('Your guess is too low.')
#   elif guess > secretNumber:
#     print('Your guess is too high')
#   else:
#     break # this is the correct guess
  
# if guess == secretNumber:
#   print('good job! You guessed the number in ' + str(guessesTaken) + ' guesses!')
# else:
#   print('Nope. The number I was thinking was ' + str(secretNumber))

# Rock paper scissors
# import random, sys

# print('rock, paper, scissors')

# # these variables keep track of the number of wins, losses, and ties
# wins = 0
# losses = 0
# ties = 0

# while True: # The main game loop.
#  print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
#  while True: # The player input loop.
#   print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
#   playerMove = input()
#   if playerMove == 'q':
#     sys.exit() # Quit the program.
#   if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
#     break # Break out of the player input loop.
#   print('Type one of r, p, s, or q.')

#  # Display what the player chose:
#  if playerMove == 'r':
#   print('ROCK versus...')
#  elif playerMove == 'p':
#   print('PAPER versus...')
#  elif playerMove == 's':
#   print('SCISSORS versus...')

#  # Display what the computer chose:
#  randomNumber = random.randint(1, 3)
#  if randomNumber == 1:
#   computerMove = 'r'
#   print('ROCK')
#  elif randomNumber == 2:
#   computerMove = 'p'
#   print('PAPER')
#  elif randomNumber == 3:
#   computerMove = 's'
#   print('SCISSORS')

#  # Display and record the win/loss/tie:
#  if playerMove == computerMove:
#   print('It is a tie!')
#   ties = ties + 1
#  elif playerMove == 'r' and computerMove == 's':
#   print('You win!')
#   wins = wins + 1
#  elif playerMove == 'p' and computerMove == 'r':
#   print('You win!')
#   wins = wins + 1
#  elif playerMove == 's' and computerMove == 'p':
#   print('You win!')
#   wins = wins + 1
#  elif playerMove == 'r' and computerMove == 'p':
#   print('You lose!')
#   losses = losses + 1
#  elif playerMove == 'p' and computerMove == 's':
#   print('You lose!')
#   losses = losses + 1
#  elif playerMove == 's' and computerMove == 'r':
#   print('You lose!')
#   losses = losses + 1

#Quiz Question 9
# spam = int(input())
# if spam == 1:
#   print('hello')
# elif spam == 2:
#   print('Howdy')
# else:
#   print('Greetings')

#Quiz 13
# for i in range(10):
#   print (i)
# print('-----------')
# i = 0
# while i < 10:
#   print(i)
#   i = i + 1
