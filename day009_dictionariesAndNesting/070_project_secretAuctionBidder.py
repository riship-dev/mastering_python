from os import system


def find_max_bidder(bids):
    maxBid = 0
    maxBidder = ""

    for bidder in bids:
        if bids[bidder] > maxBid:
            maxBid = bids[bidder]
            maxBidder = bidder
    
    return maxBidder


def silent_auction():
    number_of_participants = int(input("Number of participants?: "))
    bids = {}

    while number_of_participants > 0:
        name = input("Your name?: ")
        bid = float(input("your bid?: $"))

        bids[name] = bid

        number_of_participants -= 1
        system("cls")

    print(f"Winner: {find_max_bidder(bids)} with amount {bids[find_max_bidder(bids)]}")


silent_auction()