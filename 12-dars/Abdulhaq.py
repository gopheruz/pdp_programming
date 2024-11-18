letters = range(65, 91)
a = int(input("bir qatorda nechta harf: "))
i = 0
count = 1
for i in letters:
    print(chr(i), end=" ")
    if count != a:
        count +=1
    else:
        print()
        count = 1
