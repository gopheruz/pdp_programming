a = int(input("a: "))
b = int(input("b: "))
countOdd = 0
countEven = 0

for i in range(a, b):
    if i % 2 == 0:
        countEven += 1
    else:
        countOdd += 1

print(f"Even numbers: {countEven}")
print(f"Odd numbers: {countOdd}")