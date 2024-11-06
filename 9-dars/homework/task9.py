x = [1, 2, 0, 14, 5, -6]
a = int(input("a: "))
i = 0
has = False
while i < len(x):
	if a == x[i]:
		has = True
		i = len(x) + 1
	i += 1
print(has) 
