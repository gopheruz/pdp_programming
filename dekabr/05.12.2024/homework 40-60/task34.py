def FactN(n):
    if n < 0:
        return
    summ = 1
    for i in range(1,n+1):
        summ *= i

    return summ

print(FactN(5))
print(FactN(7))
print(FactN(12))