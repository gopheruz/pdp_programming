def Power2(a, n):
    b = a
    if a < 0:
        b = b * -1
    summ = 1

    for i in range(n):
        summ *= b
    if a < 0:
        return 1/summ
    return summ


print(Power2(-4, 10))
print(Power2(12, 4))