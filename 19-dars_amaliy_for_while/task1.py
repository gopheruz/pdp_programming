row = int(input("row: "))
col = int(input("col: "))

for i in range(1, row+1 ):
    for j in range(1, col +1):
        if j == i or i + j == col +1:
            print(f"{j}", end=" ")
        else:
            print(" ", end=" ")
    print()