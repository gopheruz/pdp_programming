import random
matrix = [[random.randint(10, 99) for _ in range(5)] for _ in range(5)]
maxnumbers = []
for i in matrix:
    maxX = i[0]
    for j in i:
        if j > maxX:
            maxX = j
        print(j, end=" ")
    print(f" max elementi: {maxX}")
