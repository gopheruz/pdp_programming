price = float(input("Konfetning narxi: "))
start = 0.2
stop = 2.0
while start < stop:
    print(f"{start:.2f} kg konfet narxi: {(start) * price:.2f}")
    start += 0.2