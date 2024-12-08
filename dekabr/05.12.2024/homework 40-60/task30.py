def DigitNK(k, n):
    while k > 0:
        if k % 10 == n:
            return k
        k /= 10
    return -1