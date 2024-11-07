start = 100
stop = 1000
while start < stop:
    ones = start % 10
    tens = (start // 10) % 10
    hundreds = start // 100
    summ = ones + tens + hundreds
    if summ % 2 != 0:
        print(start)
    start += 1
