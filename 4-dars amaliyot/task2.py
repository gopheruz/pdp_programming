son = int(input("3 xonlai son kiritin: "))
ones = son % 10
tens = (son // 10)  %10
hundreds = son // 100
isequal = (tens < hundreds)
print(isequal)