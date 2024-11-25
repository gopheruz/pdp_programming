n = int(input("n: "))
factorial = 1
yigindi = 0
for i in range(1, n + 1):
    factorial = factorial * i
    yigindi += factorial
print(yigindi)