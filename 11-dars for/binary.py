number  = int(input("Son kiriting: "))
bin = ""
while number > 0:
    reminder = number % 2
    bin = str(reminder) + bin
    number //= 2

print(bin)