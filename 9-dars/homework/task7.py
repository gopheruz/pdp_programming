x = [1, 2, 0, 14, 5, -6]

minX = x[0]
maxX = x[0]
i = 0
while i < len(x):
	if minX > x[i]:
		minX = x[i]
	if maxX < x[i]:
		maxX = x[i]
	i += 1
print(maxX, minX)
