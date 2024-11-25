input_row = int(input())
input_column = int(input())

for i in range(1, input_row+1):
    for j in range(1, input_column+1):
        if (
             ( j + i == input_column + 1 )
            or i ==1 or j == 1 or i == input_row or j == input_column
        ):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
