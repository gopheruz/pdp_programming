a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

mx = max(a, b, c)

mn = min(a, b, c)

if a < b < c or c < b <a:
    a, b, c = a * 2, b * 2, c * 2
else:
        a, b, c = ~a+1, ~b+1 , ~c+1
print(a)
print(b)
print(c)
