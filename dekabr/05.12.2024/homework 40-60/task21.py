def SummrangeAB(a,b):
    if a > b:
        return
    summ = 0

    for i in range(a,b+1):
        summ += i
    return summ

a = int(input())
b = int(input())
c = SummrangeAB(a,b)
print(c)