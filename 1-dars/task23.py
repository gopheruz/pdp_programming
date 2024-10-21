n = int(input("Kunboshidan qancha sekund o'tdi: "))

minut = n // 60
soat = (n / 60) // 60
sekund = n % 60

print(f"Kun boshidan boshlab {soat} soat {minut} minut {sekund}  sekund o'tdi")