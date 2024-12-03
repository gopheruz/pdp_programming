def Tringel(k1, k2):
    gipatenuza = ((k1*k1) + (k2*k2)) * 0.5
    return gipatenuza + k1 + k2

kated1 = int(input("kated1: "))
kated2 = int(input("kated2: "))

print(f"Perimetr: {Tringel(kated1, kated2):.2f}")
