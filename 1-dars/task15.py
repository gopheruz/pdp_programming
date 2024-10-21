# 15-masala
num = int(input("3 xonali son: "))
hundreds = num // 100
tens = (num // 10) % 10
ones = (num % 100) % 10

result = (tens  * 100) + (hundreds * 10) + ones

print(f"natija: {result}")
