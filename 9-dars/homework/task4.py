x = [1, 2, 3, 14, 5, 6, 6, 7]
max = x[0]
i = 0
while i < len(x):
	if max < x[i]:
		max = x[i]
	i += 1
print(max) 
