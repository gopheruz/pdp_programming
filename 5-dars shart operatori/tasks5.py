a = int(input("a: "))
b = int(input("d: "))
c = int(input("c: "))
musbatcount = 0
manfiycount = 0
if a > 0:
    manfiycount+=1
elif b > 0:
    manfiycount+=1
elif c > 0:
    manfiycount+=1
if a < 0:
    manfiycount+=1
elif b < 0:
    manfiycount+=1
elif c < 0:
    manfiycount+=1

print(manfiycount)
print(musbatcount)