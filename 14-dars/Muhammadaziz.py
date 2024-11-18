a = [1, 0, 5, -1, 5, 3, 1, 6]
data = []
stop = len(a) // 2
start = 0
while start < stop:
    data.append(a[start] + a[len(a) - 1 - start])
    start += 1

print(data)
