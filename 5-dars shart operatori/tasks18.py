a = int(input("1-son: "))
b = int(input("2-son: "))
c = int(input("3-son: "))
d = int(input("4-son: "))

if a == b == c:
    print("tartibi 4")
elif a == b == d:
    print("tartibi 3")
elif a == c == d:
    print("tartibi 2")
else:
    print("tartibi 1")
