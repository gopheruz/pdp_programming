n = int(input("n: "))
a = int(input("a: "))
summa = 0

for i in range(1, n+1):
    a *= i
    summa += a
print(summa)