numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
newNumbers = []
for i in range(len(numbers)):
    if numbers[i] % 2 != 0:
        newNumbers.append(numbers[i])

print(newNumbers)