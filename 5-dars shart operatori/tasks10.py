a = int(input("a: "))
b = int(input("b: "))
if a == b:
    a , b = 0, 0
else:
    b , a = a + b
print(a)
print(b)

