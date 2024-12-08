def reverSenumber(n):
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    return rev
def Ispalindrome(n):
    if n < 0:
        return False
    return n == reverSenumber(n)
print(Ispalindrome(12321))