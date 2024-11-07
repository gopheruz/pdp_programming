number1 = int(input("num1: "))
number2 = int(input("num2: "))
start = 1
summ1 = 0
while start < number1:
    if (number1 % start) == 0:
        summ1 += start
    start +=1
start = 1
summ2 = 0
while start < number2:
    if( number2 % start ) == 0:
        summ2 += start
    start += 1

print(summ1 == number2 and summ2 == number1)

