def DigitCountSum(number):
    xona = 0
    raqamlaryigindisi = 0

    while number > 0:
        a = number % 10
        raqamlaryigindisi += a
        number //= 10
        xona +=1
    return raqamlaryigindisi, xona
print(DigitCountSum(1243))