evens = 0
odds = 0

for i in range(1, 101):
    if i % 2 == 0:
        evens += 1
    else:
        odds += 1
print(odds)
print(evens)
