a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
d = int(input("d: "))
tengEmas = 0
if a == b and a == c and a != d:
    tengEmas = d


if a == b and b == d and a != c:
    tengEmas = c


if a == c and a == d and a != b:
    tengEmas = b


if b == c and b == d and b != a:
    tengEmas = a


print(tengEmas)