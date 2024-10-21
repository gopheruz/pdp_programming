#13 - masala

num = int(input("3 xonali son: "))
hundreds = num // 100
tens = (num // 10) % 10
ones = (num % 100) % 10
result = (ones * 10) + (tens * 100) + hundreds
print(f"natija: {result}")
