swapnum = lambda a, b: (b, a)

a = int(input("a: "))
b = int(input("b: "))

print(f"a: {a}")
print(f"b: {b}")

a, b = swapnum(a, b)
print(f"a: {a}")
print(f"b: {b}")
