def FactN(n):
    if n < 0:
        return
    summ = 1
    for i in range(1,n+1):
        summ *= i

    return summ

def Fact2(n):
    if n < 0:
        return
    fact1 = FactN(n)
    fact2 = FactN(fact1)
    return fact2
print(Fact2(5))