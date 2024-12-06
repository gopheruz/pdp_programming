import os
def make_parking_zone(n):
    return [[0 for _ in range(n)] for _ in range(n)]
def print_parking(parking):
    for row in parking:
        for spot in row:
            if spot != 0:
                print("🚔", end=' ')
            else:
                print(0, end=' ')
        print()
def check_position(row, col, parking):
    return parking[row][col] == 0
def add_car(row, col, parking, car_name):
    if check_position(row, col, parking):
        parking[row][col] = car_name
        return True
    return False
def recommended_spaces(row, col, parking, n):
    empty_spaces = []
    for i in range(n):
        for j in range(n):
            if parking[i][j] == 0:
                distance = abs(i - row) + abs(j - col)
                empty_spaces.append((distance, i, j))
    empty_spaces.sort()
    return empty_spaces[:10]


def input_value(prompt):
    while True:
        try:
            value = int(input(f"{prompt}: "))
            return value
        except ValueError:
            print("Please enter a valid number.")


def remove_car(row, col, parking):
    if not check_position(row, col, parking):
        car_name = parking[row][col]
        confirmation = input(f"There is a car ({car_name}) here. Remove it? (y/n): ")
        if confirmation.lower() == 'y':
            parking[row][col] = 0
            return True
    return False


def main():
    size_of_parking_zone = input_value("Enter size of parking zone")
    parking_zone = make_parking_zone(size_of_parking_zone)
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print_parking(parking_zone)

        adding = input("Add a car? (y/n): ").lower()
        if adding == "y":
            row = input_value("Enter row")
            col = input_value("Enter column")
            car_name = input("Enter car name: ")

            if row >= size_of_parking_zone or col >= size_of_parking_zone:
                print("Invalid position! Please choose a valid spot.")
                continue

            if add_car(row, col, parking_zone, car_name):
                print("Car added successfully!")
            else:
                print("Spot occupied. Recommended spaces:")
                recommendations = recommended_spaces(row, col, parking_zone, size_of_parking_zone)
                for rec in recommendations:
                    print(f"Distance: {rec[0]}, Row: {rec[1]}, Column: {rec[2]}")

        # Remove car
        removing = input("Remove a car? (y/n): ").lower()
        if removing == "y":
            row = input_value("Enter row")
            col = input_value("Enter column")

            if row >= size_of_parking_zone or col >= size_of_parking_zone:
                print("Invalid position! Please choose a valid spot.")
                continue

            if remove_car(row, col, parking_zone):
                print("Car removed successfully!")
            else:
                print("No car removed.")

        # Continue or exit
        continue_program = input("Continue? (y/n): ").lower()
        if continue_program != "y":
            break


if __name__ == "__main__":
    main()
