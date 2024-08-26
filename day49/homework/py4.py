max_bid = int(input("Enter max bid; "))

while True:
    bid = int(input("Enter bid: "))
    if bid >= max_bid:
        print("SOLD:", bid)
        break