a = int(input("a: "))
b = int(input("b: "))
counter =  0
if a <= b:
    print("a katta b fan bo'lishi kerak")
else:
    while a >= b:
        a -= b
        counter += 1

    print(f"A kesmada B {counter} marta yotadi")