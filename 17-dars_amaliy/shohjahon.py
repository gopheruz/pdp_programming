from itertools import count

input_row = int(input())
input_column = int(input())

for i in range(1, input_row+1):
    for j in range(1, input_column+1):
        if (
             ( i == j )
        ):

            print(f"{j}", end=" ")
        else:
            print(" ", end=" ")
    print()