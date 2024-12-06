def rectPs(x1, y1, x2, y2):
    eni = abs(x2 - x1)
    boyi = abs(y2 - y1)
    yuza = boyi * eni
    perimetr = 2 * (boyi + eni)
    return yuza, perimetr
x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))
yuza, perimetr = rectPs(x1, y1, x2, y2)
print(f"yuza: {yuza}")
print(f"perimetr: {perimetr}")