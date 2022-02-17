from art import logo


def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
'+': add, 
'-': subtract,
'*': multiply,
'/': divide,
}

def calculator():
  print(logo)

  num1 = float(input("What is the first number?: "))
  run = True
  while run: 
    for e in operations:
      print(e)
    perform = input("Type a math operation: ") 
    num2 = float(input("What is the next number?: "))

    calculation = operations[perform]
    answer = calculation(num1, num2)

    print(f"{num1} {perform} {num2} = {answer}")
    print(f"Type 'y' to continue calculating with {answer}, type 'n' to exit or type 'new' for a brand new calculation")
    continue_calc = input("Type y/n/new: ")
    if continue_calc == 'y':
      run = True
      num1 = answer
    elif continue_calc == 'n':
      run = False
      print("\nGoodbye.")
    elif continue_calc == 'new':
      calculator()
    else:
      print("Invalid response.")
      run = False
      print("\nGoodbye.")
calculator()
