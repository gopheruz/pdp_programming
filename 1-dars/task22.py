n = int(input("Kunboshidan qancha sekund o'tdi: "))

minut = n / 60
soat = minut // 60
sekund = n % 60

print(f"Kun boshidan boshlab {soat} soat va {sekund}  sekund o'tdi")