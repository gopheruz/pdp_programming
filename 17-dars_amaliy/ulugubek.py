input_row = int(input())
input_column = int(input())

for i in range(1, input_row+1):
    for j in range(1, input_column+1):
        if (
             (i == j )
            or ( j == (input_column - i + 1)  )
            or ( j == input_column or j == 1)
        ):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
