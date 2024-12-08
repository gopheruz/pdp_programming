def Ispower5(a):
    res = 1
    while res <= a:
        res *= 5
        if res == a:
            return True
    return False

print(Ispower5(25))
