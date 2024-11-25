from itertools import count

input_row = int(input())
input_column = int(input())

for i in range(0, input_row):
    for j in range(0, input_column):
        print(chr(i+j+65), end=" ")
    print()