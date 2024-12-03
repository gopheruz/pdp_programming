
mean = lambda a, b: (a + b) / 2
geometric_mean = lambda x, y: (x * y) **  0.5
a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))
d = int(input("D: "))

print(mean(a, b))
print(mean(a, c))
print(mean(a, d))
print("\n\n")

print(geometric_mean(a, b))
print(geometric_mean(a, c))
print(geometric_mean(a, d))