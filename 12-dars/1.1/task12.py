stop = float(input("n: "))
start = 1.1
summ  = 1.0
while start < stop:
    summ += start
    start += 0.1
print(f"{summ:.2f}")