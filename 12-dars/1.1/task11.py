n = int(input("n: "))
s = n * n
for i in range(1, n):
    s += ((n + i) * (n + i))

print(s)