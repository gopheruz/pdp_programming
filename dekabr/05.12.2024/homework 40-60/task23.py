def QuarterocCoorodinaties(x, y):
    if x > 0 < y:
        return 1
    elif x < 0 < y:
        return 2
    elif y < 0 > x:
        return 3
    elif x > 0 > y:
        return 4


print(QuarterocCoorodinaties(-1,2))