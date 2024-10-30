a = int(input("a: "))
b = int(input("b: "))
if a > b:
    a , b = b, a
else:
    b , a = a, b
print(a)
print(b)

