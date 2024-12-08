import math

def Exp1(x, epsilon):
    term = 1  # Birinchi had (x^0 / 0!)
    total = term  # Yig‘indini boshlash
    n = 1  # Indeks (1 dan boshlanadi)

    while abs(term) > epsilon:  # Had |epsilon|-dan katta bo‘lsa, davom etadi
        term *= x / n  # Yangi hadni hisoblash
        total += term  # Yig‘indiga qo‘shish
        n += 1  # Indeksni oshirish

    return total

# Namuna
x = 2  # x qiymati
epsilon1 = 0.1
epsilon2 = 0.01
epsilon3 = 0.001

print(Exp1(x, epsilon1))  # ε = 0.1 uchun natija
print(Exp1(x, epsilon2))  # ε = 0.01 uchun natija
print(Exp1(x, epsilon3))  # ε = 0.001 uchun natija
