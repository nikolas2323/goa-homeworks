time = int(input("Enter a number from 10 to 21: "))

day = int(input("Enter a number from 1 to 7: "))

if time < 10:
    print("Closed")

    if time >=10 and time <= 21:
        print("Open")
            
        if day == 6 or 7:
            print("Closed")

        else:
            print("Open")