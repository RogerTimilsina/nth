print("-------------------------------------------------")
print("WELCOME TO THE SECRET AUCTION PROGRAM")
print("-------------------------------------------------")
logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''


def highest_bidder(bid_rec):
    """Takes the bidding record and checks who is
    the winner"""
    highest_bid = 0
    winner = "no one"
    for bidder in bid_rec:
        bid_amount = bid_rec[bidder]
        if bid_amount > highest_bid:         # or winner = max(bid_rec, key=bid_rec.get) as it returns key with max val
            highest_bid = bid_amount
            winner = bidder
    print(bid_rec)
    return winner


entry = {}
ask = True
while ask:
    print(logo)
    name = input("What is your name? \n")
    price = int(input("What is your bid? \n$"))
    entry[name] = price
    Choice = input("Are there other bidders? : (Y/N)").lower()
    if Choice == "n":
        ask = False
    print("\n"*20)

bid_winner = highest_bidder(entry)
print(f"The winner of the auction is : {bid_winner}")
