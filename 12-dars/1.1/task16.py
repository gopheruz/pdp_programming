a = int(input("son: "))
n = int(input("n: "))

power = 1
for i in range(1, n + 1):
    power *= a
    print(f"{a} ing {i} - darajasi = {power}")