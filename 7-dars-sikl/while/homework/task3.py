n = int(input("n: "))
k = int(input("k: "))
counter =  0


while n > k:
    n -= k
    counter += 1

print(f"qoldiq: {n} bo'linma: {counter}")