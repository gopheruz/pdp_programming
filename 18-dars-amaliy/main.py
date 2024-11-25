input_row = int(input())
input_column = int(input())
k = 0
for i in range(0, input_row):
    for j in range(0, input_column):
        if (
                # (i + j) % 2 == 0 or
            i == j
        ):
            print(" ", end=" ")
        else:
            print("*" , end=" ")
        k = k + 1
    print()