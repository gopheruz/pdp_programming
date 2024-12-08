def IspowerN(a, n):
    res = 1
    while res <= a:
        res *= n
        if res == a:
            return True
    return False

print(IspowerN(25, 5))
