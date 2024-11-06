
data = []

while True:
	a = input("a: ")
	if a.isdigit():
		data.append(int(a))
	else:
		break
print(data)
