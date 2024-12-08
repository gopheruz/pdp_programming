def DigitCount(k):
    summ = 0
    while k > 0:
        k = k//10
        summ += 1
    return summ


print(DigitCount(12345678))