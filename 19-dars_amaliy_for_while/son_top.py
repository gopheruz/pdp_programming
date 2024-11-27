import random
number = random.randint(1, 100)
print("Men 1 dan 100 gacha bo'lgan bitta son o'yladim.")
trying = int(input("Nechta urinishda topasiz: "))
for i in range(1, trying + 1):
    guess = int(input(f"{i}-urinishingiz: Men o'ylagan son nechchi? "))
    if guess > number:
        print("Men o'ylagan son kichik.")
    elif guess < number:
        print("Men o'ylagan son katta.")
    else:
        print("Tabriklayman! Siz sonni topdingiz!")
        break
else:
    print(f"Siz yutqazdingiz. Men o'ylagan son {number} edi.")