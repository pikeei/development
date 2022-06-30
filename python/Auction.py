
import os
from turtle import clear
import art_for_auction

def highest_bidder(bidding_record):
    highest_bid=0
    winner=""   
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
    winner+=bidder
    print(f"the winner is {winner} with amount of ${highest_bid}")    
    
print(art_for_auction.logo)    
bids = {}
bidding = False 
while not bidding:
    name = input("What's your name?: ")
    price = int(input("How much is your bid?:$ "))
    bids[name] = price
    other_user = input("is there other bidder?")
    if other_user=="no":
        bidding = True
        highest_bidder(bidding_record=bids)
    elif other_user=="yes":
        clear
    
        
    
   
