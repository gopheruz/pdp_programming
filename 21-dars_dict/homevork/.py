
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
    "New York": 8175133,
    "Los Angeles": 3792621,
    "Chicago": 2695598,
    "Houston": 2327463,
    "Phoenix": 1690000,
    "Philadelphia": 1584200,
    "San Antonio": 1551000,
    "San Diego": 1423851,
    "Dallas": 1343573,
    "San Jose": 1035317,
    "London": 8908081,
    "Berlin": 3669491,
    "Madrid": 3223334,
    "Rome": 2872800,
    "Paris": 2140526,
    "Istanbul": 15462452,
    "Moscow": 12506468,
    "Tokyo": 13929286,
    "Seoul": 9776000,
    "Beijing": 21540000,
    "Shanghai": 24240000,
    "Mumbai": 12442373,
    "Jakarta": 10550000,
    "Bangkok": 8305218,
    "Karachi": 15741000,
    "Cairo": 9842000,
    "Lagos": 14000000,
    "Johannesburg": 5747000,
    "Sydney": 5312163,
    "Melbourne": 5078193,
    "Toronto": 2731571,
    "Vancouver": 631486,
    "Mexico City": 9209944,
    "Sao Paulo": 12325232,
    "Rio de Janeiro": 6748000,
    "Buenos Aires": 2890151,
    "Lima": 8773101,
    "Santiago": 5743719,
    "Bogota": 7858400,
    "Caracas": 2821256,
    "Havana": 2141652,
    "Quito": 2011388,
    "Manila": 1780148,
    "Hanoi": 8005377,
    "Kuala Lumpur": 1803452,
    "Singapore": 5453600
}


def sortDict(data):
    data = list(data.items())
    for i in range(len(data)):
        for j in range(len(data)-1-i):
            if data[j][1] > data[j+1][1]:
              data[j], data[j+1] = data[j+1], data[j]
    return dict(data)



sorted_cities_population = sortDict(cities_population)

for k, v in sorted_cities_population.items():
    print(k, v)












