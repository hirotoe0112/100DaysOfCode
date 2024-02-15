import os
from blind_auction_art import logo

os.system("cls")

print(logo)

bids = {}
bidding_finished = False
while not bidding_finished:
    bidder_name = input("What is your name?: ")
    while bidder_name in bids:
        print("You've already made a bid.")
        bidder_name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    while bid < 0:
        print("You can't bid a negative number.")
        bid = int(input("What's your bid?: $"))
    bids[bidder_name] = bid
    exists_another_bidder = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    os.system("cls")
    if exists_another_bidder == "no":
        bidding_finished = True

highest_bid = 0
highest_bidder = []
for bidder in bids:
    if highest_bid < bids[bidder]:
        highest_bid = bids[bidder]
        highest_bidder = []
        highest_bidder.append(bidder)
    elif highest_bid == bids[bidder]:
        highest_bidder.append(bidder)

print(f"The winner is {" and ".join(highest_bidder)} with a bid of ${highest_bid}!")
