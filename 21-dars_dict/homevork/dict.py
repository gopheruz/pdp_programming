mydict = {
    "name": "Nurmuhammad",
    "surname": "Hasanov"
}

mydict["secondname"] = "Ne0"

mydict["name"] = "Nasibulloh"

del mydict["name"]
keys = mydict.keys()

numbers = {
    "bir":1,
    "ikki":2,
    "uch": 3,
    "to'rt": 4,
    "biryuzyigirma": 5
}

maxValue = 0

for k in numbers.keys():
    if maxValue < k:
        maxValue = numbers[k]

