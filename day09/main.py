from replit import clear
from art import logo


auction_info = []
auction = True

def add_new_bidder(bidder_name, bidder_amount):
    new_bidder = {}
    new_bidder["bid"] = bidder_amount
    new_bidder["name"] = bidder_name
    auction_info.append(new_bidder)

while auction:
  print(logo)
  print("Welcome to the private bidding auction")
  name  = input("What is your name?: ").title()
  bid = float(input("How much would you like to bid?: $"))
  add_new_bidder(bidder_name = name, bidder_amount = bid)

  others = input("Are there any other bidders for this auction? Type 'yes' or 'no'.\n")
  if others == 'no':
    auction = False
    highest_bidder = 0
    count = -1
    for e in auction_info:
      if e['bid'] > highest_bidder:
          highest_bidder = e['bid']
          count += 1
    winner = auction_info[count]['name']
    print(f"The highest bidder is {winner} with a ${highest_bidder}")
    print("Thank you for your participation.")
  else:
    clear()
