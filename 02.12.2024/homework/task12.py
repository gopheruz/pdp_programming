def SortInc(a, b, c):
    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a
    if b > c:
        b, c = c, b

    return a, b, c
print(SortInc(15, 2, 3))