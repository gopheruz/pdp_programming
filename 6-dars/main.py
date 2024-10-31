# 1
age = int(input("Yoshingizni kiriting: "))
if age >= 18:
    print("Voyaga yetgan")
else:
    print("Voyaga yetmagan")

# 2
grade = int(input("Bahoni kiriting (2-5): "))
if grade == 5:
    print("A'lo")
elif grade == 4:
    print("Yaxshi")
elif grade == 3:
    print("Qoniqarli")
else:
    print("Qoniqarsiz")

# 3
month = int(input("Oy raqamini kiriting (1-12): "))
if month == 12 or month == 1 or month == 2:
    print("Qish")
elif month == 3 or month == 4 or month == 5:
    print("Bahor")
elif month == 6 or month == 7 or month == 8:
    print("Yoz")
else:
    print("Kuz")

# 4
temperature = float(input("Havo haroratini kiriting: "))
if temperature > 30:
    print("Havo issiq")
elif 20 <= temperature <= 30:
    print("Havo iliq")
else:
    print("Havo sovuq")

# 5
days = int(input("Hujjat amal qilish muddati (kunlarda): "))
if days > 5:
    print("Hujjat amal qilish muddati tugadi")
else:
    print("Hujjat amal qilish muddati bor")

# 6
payment_method = input("To'lov usulini kiriting (naqt/karta): ")
if payment_method == "naqt":
    amount = float(input("Summani kiriting: "))
else:
    password = input("Parolni kiriting: ")

# 7
score = int(input("Bahoni kiriting (0-100): "))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

# 8
age = int(input("Yoshingizni kiriting: "))
if age >= 18:
    print("Kattalar")
else:
    print("Bolalar")

# 9
weather = input("Ob-havo qanday (yomg'ir/qor): ")
if weather == "yomg'ir" or weather == "qor":
    print("Ko'ylak kiyma")
else:
    print("Ko'ylak kiyish mumkin")

# 10
payment_type = input("To'lov turini tanlang (naqd/kartochka): ")
if payment_type == "naqd":
    print("Naqd to'lov tanlandi")
else:
    print("Kartochka to'lov tanlandi")

# 11
grade = int(input("Bahoni kiriting (0-100): "))
if grade >= 70:
    print("Sertifikat olishingiz mumkin")
else:
    print("Sertifikat olish imkoniyati yo'q")

# 12
month = int(input("Oy raqamini kiriting (1-12): "))
if month == 12 or month == 1 or month == 2:
    print("Qish")
elif month == 3 or month == 4 or month == 5:
    print("Bahor")
elif month == 6 or month == 7 or month == 8:
    print("Yoz")
else:
    print("Kuz")

# 13
grades = [int(input("Baho kiriting: ")) for _ in range(3)]
average = sum(grades) / 3
if average >= 4:
    print("Yaxshi")
elif average >= 3:
    print("O'rtacha")
else:
    print("Yomon")

# 14
dish = input("Tanlagan taomingizni kiriting: ")
print("Tayyorlashga kirishamiz")

# 15
car_age = int(input("Avtomobilning yoshini kiriting: "))
mileage = int(input("Avtomobil yurgan masofasini kiriting: "))
if car_age > 10:
    print("Ehtiyot qismlarni tekshiring")
else:
    print("Avtomobil yaxshi holatda")

# 16
age = int(input("Yoshingizni kiriting: "))
gender = input("Jinsingiz (erkak/ayol): ")
if age < 18:
    print("O'yinchoq")
else:
    if gender == "erkak":
        print("Soat")
    else:
        print("Zargarlik buyumi")

# 17
score = int(input("Balni kiriting: "))
if score > 100:
    print("Reytingni yangilang")
else:
    print("Reyting o'zgarishsiz")

# 18
time_of_day = int(input("Vaqtni kiriting (0-24): "))
if time_of_day < 6 or time_of_day > 18:
    print("Xayrli tun")
else:
    print("Xayrli kun")

# 19
password = input("Parolni kiriting: ")
if len(password) < 8:
    print("Parolni kuchaytiring")
else:
    print("Parol qabul qilindi")

# 20
income = float(input("Daromadingizni kiriting: "))
debt = float(input("Qarz miqdorini kiriting: "))
if income > debt:
    print("Kredit olish mumkin")
else:
    print("Kredit olish imkoniyati yo'q")

# 21
age = int(input("Yoshingizni kiriting: "))
print("Sport turini tanlang")

# 22
weight = float(input("Vazningizni kiriting (kg): "))
height = float(input("Bo'yingizni kiriting (m): "))
bmi = weight / (height ** 2)
if bmi < 18.5:
    print("Ozgan")
elif 18.5 <= bmi <= 24.9:
    print("Normal")
else:
    print("Semiz")

# 23
plan = input("Yozgi ta'til rejalaringiz bormi? (ha/yo'q): ")
if plan == "ha":
    print("Yozda sayohatga chiqamiz")
else:
    print("Uyda qolamiz")

# 24
tasks = int(input("Bajarilgan ishlar sonini kiriting: "))
if tasks > 5:
    print("Yaxshi natija")
else:
    print("Yana ishlash kerak")

# 25
book_name = input("Kitob nomini kiriting: ")
if book_name.lower() in ["harry potter", "war and peace"]:
    print("Buni o'qiganman")
else:
    print("O'qimaganman")

# 26
team = input("Sevimli futbol jamoangizni kiriting: ")
if team.lower() == "liverpool":
    print("Tabriklaymiz!")
else:
    print("Jamoangiz uchun omad")

# 27
expense = float(input("Xarajatni kiriting: "))
income = float(input("Daromadni kiriting: "))
if expense < income:
    print("Foyda")
else:
    print("Zarar")

# 28
experience = int(input("Ish tajribangizni kiriting (yillarda): "))
if experience < 2:
    print("Yosh mutaxassis")
else:
    print("Tajribali mutaxassis")

# 29
job_result = input("Ish natijasi (Qoniqarli/Yaxshi/Mukammal): ")
print(job_result)

# 30
product_value = float(input("Mahsulot qiymatini kiriting ($): "))
if product_value > 100:
    print("Boj to'lashingiz kerak")
else:
    print("Boj to'lashingiz kerak emas")

# 31
age = int(input("Yoshingizni kiriting: "))
weight = int(input("Vazningizni kiriting: "))
if age < 18 or weight > 120:
    print("Uchish mumkin emas")
else:
    print("Uchishingiz mumkin")

# 32
temperature = float(input("Haroratni kiriting: "))
if temperature < 0:
    print("Qishda qizish")
else:
    print("Harorat mos")

# 33
preparation = input("Maktabga tayyorgarligingiz qanday? (yetarli/yetarli emas): ")
if preparation == "yetarli emas":
    print("Ko'proq o'qish kerak")
else:
    print("Tayyorgarlik yaxshi")

# 34
demand = input("Savdo so'rovlarini kiriting: ")
if demand == "yuqori":
    print("Savdo muvaffaqiyatli")
else:
    print("Savdo o'rtacha")

# 35
preparation_level = input("Dars tayyorgarlik darajasini kiriting (yetarli/yetarli emas): ")
if preparation_level == "yetarli emas":
    print("Boshqa darslar oling")
else:
    print("Tayyorgarlik yaxshi")

# 36
friends = int(input("Do'stlaringiz sonini kiriting: "))
if friends < 5:
    print("Do'stlar orttirishingiz mumkin")
else:
    print("Do'stlar soni yetarli")
