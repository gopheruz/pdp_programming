n = int(input("n: "))
daraja = n-1
kv  = 1
while daraja > 0:
    kv *= 10
    daraja -= 1
start = kv
stop = kv * 10
while start < stop:
    print(start)
    start += 1

