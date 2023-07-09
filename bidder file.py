print("*********welcome to bidding*************")
import os
def find_winner(bidder_details):
    higgest_bid = 0
    winner=""
    for bidder in bidder_details:
        bidding_price = bidder_details[bidder]
        if bidding_price > higgest_bid:
            higgest_bid = bidding_price
            winner = bidder
    print(f"the winner details are {bidder} & price {higgest_bid}")
bidder_data = {}

end_of_bidding = False
while not end_of_bidding:
    name = input("ente ryour name :")
    price = int(input("enter bidding price :"))
    bidder_data[name] = price
    more_bidders = input("more bidders yes or no :").lower()
    if more_bidders == "no":
        end_of_bidding = True
        find_winner(bidder_data)

    elif more_bidders == "yes":
        os.system("cls")
print(bidder_data)