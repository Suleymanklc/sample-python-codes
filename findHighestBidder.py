from art import logo

print(logo)
print("Welcome to the game!")
bids = {}
bidding_is_finished = False


def highest_bid(bids):
    """"Please select the highest bid from here"""  
    return max(bids.values())


while not bidding_is_finished:
    bid = int(input("Enter your bid: "))
    name = input("Enter your name: ")
    bids[name] = bid
    bidover = input("Quit Y/N? :").lower()

    if bidover == "y":
        bidding_is_finished = True
    if highest_bid(bids) == bid and bidding_is_finished:
        print(f"Congratulations! You are the highest bidder! \n {bid}")

