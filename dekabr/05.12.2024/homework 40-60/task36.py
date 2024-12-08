def Fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a = 0
    b = 1
    for i in range(3, n + 1):
        temp = a
        a = b
        b = temp + a
    return b

print(Fib(34))
