def powerA234(a, p):
    if p == 2:
        return a * a
    if p == 3:
        return a * a * a
    if p == 4:
        return a * a * a * a
    return

a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))
print(powerA234(a,2))
print(powerA234(b,3))
print(powerA234(c,4))
