cities_population = {
    "Toshkent": 2737000,
    "Samarqand": 1143000,
    "Buxoro": 857000,
    "Farg'ona": 1039000,
    "Namangan": 1222000,
    "Andijon": 1185000,
    "Qo'qon": 329000,
}

new_city = input("Yangi shaharni kiriting: ")
new_population = int(input("Shahar aholisini kiriting: "))

if new_city in cities_population:
    print(f"{new_city} shahri allaqachon mavjud. Aholisi: {cities_population[new_city]}")
else:
    cities_population[new_city] = new_population
    print(f"{new_city} shahri qo'shildi. Aholisi: {new_population}")

print("\nYangi lug'at holati:")
for city, population in cities_population.items():
    print(f"{city}: {population}")
