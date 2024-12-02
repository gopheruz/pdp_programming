
parkovka = [
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

def showParkovka():
    for i in range(0,5):
        for j in range(0,5):
            print(parkovka[i][j],end=" ")
        print()

showParkovka()
while True:
    row = int(input("Row: "))
    col = int(input("Col: "))
    name_car = input("Name car: ")
    if parkovka[row][col] == 0:
        choose = input("Do you want to add Y/N: ")
        if choose == "Y":
            parkovka[row - 1][col - 1] = 1
            print(f"{name_car} add")
            showParkovka()
        else:
            print("Finish operation")
    else:
        print("This is position busy")