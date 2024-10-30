a = int(input("a: "))
b = int(input("b: "))
if a != b:
    if a > b:
        b = a
    else:
        a = b
else:
    a, b = 0, 0

print(a)
print(b)


