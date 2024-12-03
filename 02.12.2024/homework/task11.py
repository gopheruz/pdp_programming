def MinMax(x, y):
    if x > y:
        return (y, x)
    return (x, y)


print(MinMax(12, 34))