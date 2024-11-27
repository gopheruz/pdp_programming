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
    print("\nHozirgi parkovka holati:")
    for i in parking_zone:
        for j in i:
            print(j, end=" ")
        print()

    door = int(input("Qaysi eshikdan kirmoqchisiz? (1 yoki 2): "))
    if door == 1:
        startrow = 0
        startcol = 0
        row_step = 1
        col_step = 1
    elif door == 2:
        startrow = 9
        startcol = 9
        row_step = -1
        col_step = -1
    else:
        print("Xato tanlov! Iltimos, 1 yoki 2 kiriting.")
        continue

    row = int(input("Manzil qatori (1-10): ")) - 1
    col = int(input("Manzil ustuni (1-10): ")) - 1

    if parking_zone[row][col] == 0:
        car_name = input("Mashina nomini kiriting: ")
        parking_zone[row][col] = car_name
        print(f"{car_name} mashinasi ({row+1}, {col+1}) joyga qo'yildi.")
    else:
        print(f"({row+1}, {col+1}) manzilida {parking_zone[row][col]} mashinasi turibdi.")
        found = False
        r = startrow
        while 0 <= r < 10 and not found:
            c = startcol
            while 0 <= c < 10:
                if parking_zone[r][c] == 0:
                    print(f"Tavsiya qilingan joy: ({r+1}, {c+1})")
                    car_name = input("Mashina nomini kiriting: ")
                    parking_zone[r][c] = car_name
                    print(f"{car_name} mashinasi ({r+1}, {c+1}) joyga qo'yildi.")
                    found = True
                    break
                c += col_step
            r += row_step
        if not found:
            print("Parking zona to'lgan! Bo'sh joylar yo'q.")

    continue_parking = input("Mashinalarni joylashda davom etasizmi? (ha/yo'q): ").lower()
    if continue_parking != "ha":
        break
print("\nOxirgi parkovka holati:")
for row in parking_zone:
    for cell in row:
        print(cell, end=" ")
    print()
