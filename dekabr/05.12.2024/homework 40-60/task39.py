# Power1 = lambda A, B: A ** B
def Power1(A, B):
    summ = 1

    for i in range(B):
        summ *= A

    return summ


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


def Power3(a, n):
    if n % 1 != 0:
        return Power2(a, n)
    else:
        return Power1(a, n)


print(Power3(12.5, 4))