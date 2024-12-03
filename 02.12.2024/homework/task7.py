def invertDigit(number):
    teskari = ""
    while number > 0:
        a = number % 10
        teskari += str(a)
        number = number // 10
    return int(teskari)

print(invertDigit(123))
