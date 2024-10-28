a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
print((a == b and a != c) or (a == c and a != b) or (b == c and b != a))