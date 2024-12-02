n = int(input("Garage o'lchamini kiriting: "))

a = [[0] * n for i in range(n)]

while True:
    car_name = input("Mashina nomini kiriting: ")

    col = int(input("Ustunni kiriting: ")) - 1
    row = int(input("Qatorni kiriting: ")) - 1

    if a[row][col] == 0:
        a[row][col] = car_name
    else:
        empty_rows = []
        empty_cols = []
        distances = []

        for i in range(n):
            for j in range(n):
                if a[i][j] == 0:
                    empty_rows.append(i)
                    empty_cols.append(j)
                    distance = abs(i - row) + abs(j - col)
                    distances.append(distance)

        if 0 in distances:
            distances.remove(0)

        min_distance = min(distances)

        if min_distance > 5:
            continue

        while min_distance == min(distances):
            index = distances.index(min_distance)
            distances.pop(index)
            print("Siz hozirda bu yerga mashina qo'ya olmaysiz, mana bu koordinatalarga mashina qo'ysangiz bo'ladi:")
            print(empty_rows[index] + 1, empty_cols[index] + 1)
        print(f"Bu yerda {a[row][col]} bor")
        continue

    for row in a:
        print(*row)
