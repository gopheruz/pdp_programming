import os
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
    os.system("clear")
    print("Hozirgi Holati\n")

    for i in parking_zone:
        for j in i:
            print(j , end=" ")
        print()
    print("\n")
    row = int(input("qaysi qator: ")) -1
    col = int(input("qaysi ustun: ")) - 1
    car_name = input("Moshina nomi: ")
    if parking_zone[row][col] == 0:
        parking_zone[row][col] = car_name
        print(f"{car_name} mashinasi ({row+1}:{col+1}) manziliga qo'yildi")
        print("Parkovka holati\n\n")
        for i in parking_zone:
            for j in i:
                print(j , end=" ")
            print()
    else:
        print(f"{row+1}:{col+1} joyida {parking_zone[row][col]} turibdi")
        print("bo'sh joylar: \n")
        for i in parking_zone:
            for j in i:
                print(j , end=" ")
            print()

    eshmat = input("yana moshina qo'yasizmi: (ha/yo'q): ").lower()
    if eshmat != "ha":
        print("Parkovka holati\n\n")
        for i in parking_zone:
            for j in i:
                print(j , end=" ")
            print()
        break
