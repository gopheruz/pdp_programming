a = int(input("a: "))
b = int(input("b: "))

if a <= b:
    print("a katta b fan bo'lishi kerak")
else:
    while a >= b:
        a -= b

    print(f"qolgan qismi: {a}")