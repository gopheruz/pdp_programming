price = float(input("Konfetning narxi: "))
start = 0.1
stop = 1.0
while start < stop:
    print(f"{start:.2f} kg konfet narxi: {(start) * price:.2f}")
    start += 0.1