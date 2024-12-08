def Isprime(a):
    for i in range(2, a//2):
        if a % i == 0:
            return False
    return True



print(Isprime(13))