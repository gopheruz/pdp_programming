list = range(54, 69)
result = []

for i in list:
    result.append((i % 10) + i // 10)

print(result)