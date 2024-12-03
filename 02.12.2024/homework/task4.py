def triengle(a):
    yuzasi = ((a**0.5) / 4) * a**2
    peremetri = 3 * a
    return yuzasi, peremetri

a = int(input("a: "))
yuza, perem = triengle(a)

print(f"yuzasi: {yuza:.2f}\nperemetri: {perem}")