a = int(input("a: "))
b = int(input("b: "))
tempa = a
tempb  = b
while b != 0:
	temp = b
	b = a % b
	a = temp
ekuk = (tempa * tempb) // a

print(f"ekuk {ekuk}")
