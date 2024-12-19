""""parking_zone = [
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
    for i in parking_zone:
        for j in i:
            print(j, end=" ")
        print()
    row = int(input("r: ")) -1
    col = int(input("c: ")) -1
    car_name = input("car name: ")
    if parking_zone[row][col] == 0:
        parking_zone[row][col] = car_name
    else:
        print(f"({row+1}:{col+1}) joyida {parking_zone[row][col]} turibdi")
        start_row = 0
        found = True
        while 0 <= start_row < 10 and not found:
            start_col = 0
            while 0 <= start_col < 10:
                if parking_zone[start_row][start_col] == 0:
                    found = False
                    print(f"tafsiya qilingan joy: ({start_row}:{start_col}")
                    parking_zone[start_row][start_col] = car_name
                    break
                start_col += 1
            start_row += 1
    print("\n\n")"""