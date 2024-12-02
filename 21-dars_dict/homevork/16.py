cities_population = {
    "Toshkent": 2737000,
    "Samarqand": 1143000,
    "Buxoro": 857000,
    "Farg'ona": 1039000,
    "Namangan": 1222000,
    "Andijon": 1185000,
    "Qo'qon": 329000,
    "Marg'ilon": 215000,
    "Jizzax": 715000,
    "Guliston": 764000,
    "Navoiy": 452000,
    "Urganch": 416000,
    "Xiva": 275000,
    "Shahrisabz": 183000,
    "Qarshi": 682000,
    "Denov": 245000,
    "Termiz": 664000,
    "Angren": 175000,
    "Bekobod": 202000,
    "Chirchiq": 213000,
    "Olmaliq": 156000,
    "Yangiyer": 121000,
    "Kattaqo'rg'on": 150000,
    "G'ijduvon": 98000,
    "Zarafshon": 65400,
    "Chortoq": 147000,
    "Nurota": 48000,
    "Qiziltepa": 57000,
    "To‘raqo‘rg‘on": 123000,
    "Koson": 109000,
    "Ishtixon": 94000,
    "Chust": 145000,
    "Oltinko‘l": 132000,
    "Shofirkon": 110000,
    "Bulung‘ur": 125000,
    "Pop": 89000,
    "Yangiqo‘rg‘on": 117000,
    "Sho‘rchi": 78000,
    "Boysun": 67000,
    "Kasbi": 73000,
    "Qo‘shrabot": 68000,
    "Muborak": 46000,
    "Kitob": 141000,
    "Piskent": 97000,
    "Zangiota": 162000,
    "Chinoz": 122000,
    "Baliqchi": 85000,
    "Bektemir": 55000,
    "Yangibozor": 61000,
    "Oqqo‘rg‘on": 103000,
}














items = list(cities_population.items())

print(items)
for k, v in cities_population.items():
    print(f"{k}: {v}")

for i in range(len(items)):
    for j in range(len(items) - i - 1):
        if items[j][1] > items[j + 1][1]:
            items[j], items[j + 1] = items[j + 1], items[j]

sorted_data = dict(items)


print("\n\n   tartiblangan   \n")

for k, v in sorted_data.items():
    print(f"{k}: {v}")
