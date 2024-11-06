x = [1, 2, 3, 14, 5, 6, 6, 7]
maxIndex = 0
i = 0

while i < len(x):
	if x[maxIndex] < x[i]:
		maxIndex = i
	i += 1
print(maxIndex)
