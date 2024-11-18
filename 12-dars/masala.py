# 100 gram konfet 5600 som
start100gram = 100
pricePeergram = int(input("Price: "))
lastPrice = 0
while start100gram <= 1000:
    start100gram += 100
    lastPrice += pricePeergram

print(lastPrice)