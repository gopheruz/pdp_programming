lst = [1, 2, 3, 4, 5]  
element = 3 
i = 0
found = False
while i < len(lst):
    if lst[i] == element:
        found = True
    i += 1
print(found)

i = 100
while i < 1000:
    yigindi = (i // 100) + (i // 10 % 10) + (i % 10)
    if 5 < yigindi < 8:
        print(i)
    i += 1

son = int(input("Son kiriting: "))
while True:
    if son % 2 == 0:
        print("Juft son")
    else:
        print("Toq son")
    break

n = int(input("Nechta son kiritasiz: "))
i = 0
yigindi = 0
while i < n:
    son = int(input("Son kiriting: "))
    yigindi += son
    i += 1
print("Yig'indisi:", yigindi)

n = int(input("Nechta son kiritasiz: "))
i = 0
eng_katta = float('-inf')
while i < n:
    son = int(input("Son kiriting: "))
    if son > eng_katta:
        eng_katta = son
    i += 1
print("Eng katta son:", eng_katta)

n = int(input("Nechta son kiritasiz: "))
i = 0
eng_kichik = float('inf')
while i < n:
    son = int(input("Son kiriting: "))
    if son < eng_kichik:
        eng_kichik = son
    i += 1
print("Eng kichik son:", eng_kichik)

lst = [1, 2, 3, 4, 5]
i = 0
while i < len(lst):
    print(lst[i] * 2)
    i += 1

son = int(input("Son kiriting: "))
i = 1
yigindi = 0

while i < son:
    if son % i == 0:
        yigindi += i
    i += 1
if yigindi == son:
    print("Mukammal son")
else:
    print("Mukammal son emas")

son = int(input("Son kiriting: "))
i = 1
daraja = 1

while i <= son:
    if 2 ** i == son:
        print("2 ning darajasi:", i)
        daraja = 0
        break
    i += 1
if daraja:
    print("2 ning darajasi emas")

son = int(input("Son kiriting: "))
daraja = 0
i = 1
while 2 ** i <= son:
    if 2 ** i == son:
        daraja = i
        break
    i += 1
if daraja:
    print(f"Bu son 2 ning {daraja}-darajasi.")
else:
    print("Bu son 2 ning darajasi emas.")

son = int(input("Son kiriting: "))
faktorial = 1
i = 1

while i <= son:
    faktorial *= i
    i += 1
print("Faktorial:", faktorial)

x = [1, 23, 10, 45, -41, 56, 78, 13]
juft = []
toq = []
i = 0

while i < len(x):
    if x[i] % 2 == 0:
        juft.append(x[i])
    else:
        toq.append(x[i])
    i += 1
print("Juft elementlar:", juft)
print("Toq elementlar:", toq)


son = int(input("Son kiriting: "))
i = 1

while i <= 10:
    print(f"{son} x {i} = {son * i}")
    i += 1

cars = ["Audi", "Tayota", "Mazda", "Volvo", "Lada"]
i = 0
eng_uzun = ""

while i < len(cars):
    if len(cars[i]) > len(eng_uzun):
        eng_uzun = cars[i]
    i += 1
print("Eng uzun so'z:", eng_uzun)

cars = ["Audi", "Tayota", "Mazda", "Volvo", "Lada"]
i = 0


while i < len(cars):
    if cars[i].endswith("a"):
        print(cars[i])
    i += 1
