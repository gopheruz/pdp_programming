x = [-2, 31, 104, 51, 19, 7] 
print(x)
minX = 0
maxX = 0
i = 0
while i < len(x):
	if x[minX] > x[i]:
		minX = i
	if x[maxX] < x[i]:
		maxX = i
	i += 1

temp = x[maxX]
x[maxX] = x[minX]
x[minX] = temp

print(x)
