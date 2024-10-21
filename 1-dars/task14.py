#14- masala
num = int(input("3 xonali son: "))
hundreds = num // 100
tens = (num // 10) % 10
ones = (num % 100) % 10
result = (ones * 100) + tens + (hundreds * 10)
print(f"natija: {result}")
