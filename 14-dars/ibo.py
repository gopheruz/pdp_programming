a = [1,0,5,-1,5,3,1,6]
b = []
start = 1
while start < len(a):
    b.append(a[start-1] + a[start])
    start += 1
print(b)