a = int(input("A nuqtasi: "))
b = int(input("B nuqtasi: "))
c = int(input("C nuqtasi: "))

dist_AB = abs(b - a)  
dist_AC = abs(c - a)  

if dist_AB < dist_AC:
    print("A nuqtaga eng yaqin nuqta: B")
else:
    print("A nuqtaga eng yaqin nuqta: C")
