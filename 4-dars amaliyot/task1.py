son = int(input("3 xonlai son kiritin: "))
ones = son % 10
tens = (son // 10)  %10
hundreds = son // 100
res = ones + hundreds
isequal = (res == ones or res == tens or res == hundreds)
print(isequal)