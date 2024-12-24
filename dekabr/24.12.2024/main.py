class Hodim:
    def __init__(self, ism, maosh, yoshi, ishstaji, lavozimim):
        self.ism = ism
        self.maosh = maosh
        self.yoshi = yoshi
        self.ishstaji = ishstaji
        self.lavozimim = lavozimim
    def __str__(self):
        return f"Ism: {self.ism}\nMaoshi: {self.maosh}\nYoshi: {self.yoshi}\nIsh tajriba: {self.ishstaji}\nLavozimi: {self.lavozimim}"



# Doniyor = Hodim(
#     ism="Doniyor",
#     maosh=5600,
#     yoshi=20,
#     ishstaji=2,
#     lavozimim="Beckendchi"
# )
#
# Alex = Hodim("Alex", 1400, 28, 2, "UXUI")
#
# print(Alex)

count = int(input("Siz neshta xodim yaratmoqchisiz: "))
i = 1

while i <= count:
    ism = input(f"{i}-xodim ism: ")
    maosh = float(input(f"{ism}ni maosh: "))
    yoshi = int(input(f"{ism}ni yoshi: "))
    ishstaji = int(input(f"{ism}ni ishstaji: "))
    lavozimim = input(f"{ism}ni lavozimi: ")
    hodim = Hodim(ism, maosh, yoshi, ishstaji, lavozimim)
    i +=1
