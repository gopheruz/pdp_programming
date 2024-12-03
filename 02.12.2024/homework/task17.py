def Kvadrat_ildizlari(A, B, C):
    if A == 0:
        return "A cannot be zero."
    diskrminat =( B ** 2 )- (4 * A * C)

    if diskrminat > 0:
        return "Kvadrat tenglamani 2 ta ildizi bor "
    elif diskrminat == 0:
        return "Teglamani bita ildizi bor."
    else:
        return "Ildizi yo'q"

A = 1
B = -3
C = 2
print(Kvadrat_ildizlari(A, B, C))