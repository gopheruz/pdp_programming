# UsaCar =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# GermanCar = UsaCar.copy()
# UsaCar.clear()
# GermanCar["brand"] = "Mercedec"
# print(UsaCar)



parking_zone = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
]
for i in parking_zone:
    print(i)

parking_zone[2][5] = "Onix"

print("\n\n\n")

for i in parking_zone:
    print(i)