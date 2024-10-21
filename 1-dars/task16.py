#16-masala
num = int(input("3 xonali son: "))
hundreds = num // 100
tens = (num // 10) % 10
ones = (num % 100) % 10
result = (hundreds * 100 ) + (ones * 10) + tens
print(f"natija: {result}")
