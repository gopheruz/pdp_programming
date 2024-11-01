Auto_price = int(input("Avtomobil narxi: "))
first_precent = float(input("Necha foiz oldindan to'laysiz (0-100)%: "))
month = int(input("Necha oyga olasiz: "))

if first_precent < 0 or first_precent > 100:
    print("Iltimos, 0 dan 100 gacha bo'lgan foizni kiriting.")


elif first_precent < 29:
    print("Kamida 30 % to'lashingiz kerak.")


elif first_precent > 29 and  first_precent < 40:
    qarz = Auto_price - (Auto_price * first_precent) / 100
    interest_rate = 23.5 / 100.0  
    interest = (Auto_price - qarz) * interest_rate  
    foziPlusQarz = qarz + interest  
    perrMonth = foziPlusQarz / month
    print(f"Qarz:        {qarz:.2f} so'm")
    print(f"Fozi + Qarz: {foziPlusQarz:.2f} so'm")
    print(f"Oyiga        {perrMonth:.2f} so'm to'laysiz")

elif first_precent > 39 and first_precent < 50:
    qarz = Auto_price - (Auto_price * first_precent) / 100
    interest_rate = 17.5 / 100.0  
    interest = (Auto_price - qarz) * interest_rate  
    foziPlusQarz = qarz + interest  
    perrMonth = foziPlusQarz / month
    print(f"Qarz:        {qarz:.2f} so'm")
    print(f"Fozi + Qarz: {foziPlusQarz:.2f} so'm")
    print(f"Oyiga        {perrMonth:.2f} so'm to'laysiz")


elif first_precent > 49:
    qarz = Auto_price - (Auto_price * first_precent) / 100
    interest_rate = 10 / 100.0  
    interest = (Auto_price - qarz) * interest_rate  
    foziPlusQarz = qarz + interest  
    perrMonth = foziPlusQarz / month
    print(f"Qarz:        {qarz:.2f} so'm")
    print(f"Fozi + Qarz: {foziPlusQarz:.2f} so'm")
    print(f"Oyiga        {perrMonth:.2f} so'mdan to'laysiz")
else:
    print("Kutilmagan xatolik: ")