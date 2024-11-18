n = int(input("n: "))
summa = 0
ishora = 1
for i in range(1, n + 1):
    summa += (ishora * i)
    ishora *= -1

print(f"{summa:.1f}")