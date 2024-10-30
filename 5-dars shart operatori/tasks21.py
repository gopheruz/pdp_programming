x = int(input("x: "))
y = int(input("y: "))

if y > 0 and x > 0:
    print("2- chorak")
elif y > 0 and x < 0:
    print("1- chorak")
elif y < 0 and x > 0:
    print("4- chorak")
elif x * y > 0:
    print("3- chorak")
else:
    print("Koordinata boshi")

