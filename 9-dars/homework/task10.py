a = int(input("a: "))
b = int(input("a: "))

while b != 0:
    temp = b
    b = a % b
    a = temp
print(f"ekub: {a}")
