# Define the parking zone
parking_zone = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

while True:
    # Print the parking zone
    print("\nCurrent Parking Zone:")
    for row in parking_zone:
        for cell in row:
            print(cell, end=" ")
        print()

    # Ask which door the user is entering from
    door = input("Which door do you use for entering (1 for top-left, 2 for bottom-right)? ")
    if door == "1":
        print("You entered from the top-left corner (0, 0).")
        start_row, start_col = 0, 0
        row_step, col_step = 1, 1  # Search top-left to bottom-right
    elif door == "2":
        print("You entered from the bottom-right corner (9, 9).")
        start_row, start_col = 9, 9
        row_step, col_step = -1, -1  # Search bottom-right to top-left
    else:
        print("Invalid choice. Please enter 1 or 2.")
        continue

    # Ask for the parking spot
    row = int(input("Enter the row number (0-9): "))
    col = int(input("Enter the column number (0-9): "))

    # Check if the spot is empty
    if parking_zone[row][col] == 0:
        car_name = input("Enter the car name: ")
        parking_zone[row][col] = car_name
        print(f"Car '{car_name}' parked at ({row}, {col}).")
    else:
        print(f"The spot ({row}, {col}) is already full.")
        # Find the next available spot starting from the door
        found = False
        r = start_row
        while 0 <= r < 10 and not found:
            c = start_col
            while 0 <= c < 10:
                if parking_zone[r][c] == 0:
                    print(f"Suggested place: ({r}, {c})")
                    car_name = input("Enter the car name: ")
                    parking_zone[r][c] = car_name
                    print(f"Car '{car_name}' parked at ({r}, {c}).")
                    found = True
                    break
                c += col_step
            r += row_step
        if not found:
            print("Parking zone is full. No available spots.")

    continue_parking = input("Do you want to park another car? (yes/no): ").strip().lower()
    if continue_parking != "yes":
        break

print("\nFinal Parking Zone:")
for row in parking_zone:
    for cell in row:
        print(cell, end=" ")
    print()
