a = int(input("a: "))
n = int(input("n: "))

ishora = -1
summa = 1

for i in range(1, n+1):
    summa += ishora * (a ** i)
    ishora *= -1
print(summa)