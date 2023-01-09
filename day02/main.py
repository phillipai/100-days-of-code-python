print("Welcome to the tip calculator!")

bill = float(input("What is the total bill amount?\n$:")) # takes input of float data type 
tip = int(input("How much tip would you like to give?\nPercent:")) # takes input of int data type 
split = int(input("How many people to split the bill?\nPeople:"))

total = ("{:.2f}".format((((bill * (tip / 100)) + bill) / split))) 

print(f"Each person should pay: ${total}")
