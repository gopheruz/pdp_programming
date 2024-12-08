# Power1 = lambda A, B: A ** B
def Power1(A, B):
    summ = 1

    for i in range(B):
        summ *= A

    return summ


print(Power1(2,2))