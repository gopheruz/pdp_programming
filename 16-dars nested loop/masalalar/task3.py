row = int(input("row: "))
col = int(input("col: "))
for i in range(1, row + 1):
    for j in range(1, col + 1):
        if (
                i == 1 or j == 1

                ):
                    print("#", end=" ")
        else:
            print("*", end=" ")
    print()
