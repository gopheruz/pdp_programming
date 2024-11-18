a = range(13, 30)
b = []
for i in a:
    if i > 9 and i < 100:
        b.append( (i % 10) + (i // 10))

print(b)