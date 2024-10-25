fanlar = ["programming", "ITs", "English", "Web", "buisness"]
summ = 0
for i in fanlar:
    a = int(input(f"{i} fanidan olgan bahoyingiz: "))
    summ += a
print(summ / len(fanlar) >= 4.5)