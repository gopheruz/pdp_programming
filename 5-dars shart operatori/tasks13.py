a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

mx = max(a, b, c)

mn = min(a, b, c)

mid = 0
if a != mx and a != mn:
    mid = a
elif b != mx and b != mn:
    mid = b
else:
    mid = c

print(mid)
