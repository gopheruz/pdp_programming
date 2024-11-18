# listdan toqlarni aolida 
lst = range(15, 49)
toq = []
juft = []
for i in lst:
    if i != 0 and i % 2 == 0:
        juft.append(i)
    else:
        toq.append(i)

print(toq)
print(juft)