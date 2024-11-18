n = int(input("n: "))
a = 0
b = 1
nextt = a + b
print(a)
print(b)
while nextt < n:
    print(nextt)
    a = b
    b = nextt
    nextt = a + b

