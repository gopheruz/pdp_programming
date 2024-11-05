n = int(input("n: "))

start = 10 ** (n - 1)
stop = 10 ** n

while start < stop:
    print(start)
    start += 1

