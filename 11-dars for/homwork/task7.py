matn  = input("str: ")
count = 0

for i in matn:
    if 65 <= ord(i) <=90:
        count += 1

print(count)
        