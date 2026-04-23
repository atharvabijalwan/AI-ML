ROWS = 5
COLUMNS = 10

# Initialize all seats as empty (0)
seats = [[0 for _ in range(COLUMNS)] for _ in range(ROWS)]

ticket_price = 200
revenue = 0

while True:
    print("\n        Atharva Railway System")
    print("1. Show Seat Layout")
    print("2. Book a Seat")
    print("3. Cancel a Seat")
    print("4. Show Revenue")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    
    if choice == 1:
        print("\nSeat Layout (0 = Empty, 1 = Booked):")
        for row in seats:
            for seat in row:
                print(seat, end=" ")
            print()

    
    elif choice == 2:
        print(f"\nTicket Price per Seat: {ticket_price}")

        row = int(input("Enter Row Number (1-5): "))
        column = int(input("Enter Column Number (1-10): "))

        row -= 1
        column -= 1

        if row < 0 or row >= ROWS or column < 0 or column >= COLUMNS:
            print("\nInvalid Seat Position!")

        elif seats[row][column] == 1:
            print("\nSeat Already Booked!")

        else:
            seats[row][column] = 1
            revenue += ticket_price
            print("\nSeat Booked Successfully!")

    
    elif choice == 3:
        row = int(input("Enter Row Number (1-5): "))
        column = int(input("Enter Column Number (1-10): "))

        row -= 1
        column -= 1

        if row < 0 or row >= ROWS or column < 0 or column >= COLUMNS:
            print("\nInvalid Seat Position!")

        elif seats[row][column] == 0:
            print("\nSeat is Already Empty!")

        else:
            seats[row][column] = 0
            revenue -= ticket_price
            print("\nSeat Cancelled Successfully!")

    
    elif choice == 4:
        print(f"\nTotal Revenue Earned: {revenue}")

    
    elif choice == 5:
        print("\nExiting System... Thank you!")
        break

    
    else:
        print("\nInvalid Choice! Please Try Again.")
