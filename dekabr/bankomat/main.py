def main_menu():
    while True:
        print("\nBosh menyu:")
        print("1. Balansni tekshirish")
        print("2. Naqd pul olish")
        print("3. SMS xabar ulash")
        print("4. Parolni o'zgartirish")
        print("5. Mobil aloqa uchun to'lov")
        print("6. Kredit to'lovlari")
        print("7. Komunal to'lovlar")
        print("8. Dasturdan chiqish")

        choice = input("Tanlovingizni kiriting: ")

        if choice == "1":
            check_balance()
        elif choice == "2":
            withdraw_cash()
        elif choice == "3":
            sms_settings()
        elif choice == "4":
            change_password()
        elif choice == "5":
            mobile_payment()
        elif choice == "6":
            credit_payment()
        elif choice == "7":
            utility_payment()
        elif choice == "8":
            print("Dastur tugadi.")
            break
        else:
            print("Noto'g'ri tanlov. Qayta urinib ko'ring.")


def check_balance():
    print("\nBalansni tekshirish:")
    print("Balansingizda 100000 so'm mablag' bor.")
    input("Ortga qaytish uchun Enter tugmasini bosing.")


def withdraw_cash():
    print("\nNaqd pul olish:")
    print("1. 50 ming")
    print("2. 100 ming")
    print("3. 150 ming")
    print("4. 200 ming")
    print("5. 300 ming")
    print("6. 400 ming")
    print("7. Boshqa summa")
    print("8. Orqaga")
    choice = input("Tanlovingizni kiriting: ")

    if choice == "8":
        return
    print("Tanlangan summa chiqarilmoqda...")
    input("Ortga qaytish uchun Enter tugmasini bosing.")


def sms_settings():
    print("\nSMS xabar ulash:")
    print("1. SMS xabarni o'chirish")
    print("2. SMS xabarni yoqish")
    print("3. Orqaga")
    choice = input("Tanlovingizni kiriting: ")

    if choice == "3":
        return
    print("Tanlov bajarildi.")
    input("Ortga qaytish uchun Enter tugmasini bosing.")


def change_password():
    print("\nParolni o'zgartirish:")
    new_password = input("Yangi parolni kiriting: ")
    print("Parolingiz muvaffaqiyatli o'zgartirildi.")
    input("Ortga qaytish uchun Enter tugmasini bosing.")


def mobile_payment():
    print("\nMobil aloqa uchun to'lov:")
    print("1. Uzmobile")
    print("2. Beeline")
    print("3. Ucell")
    print("4. UMS")
    print("5. Perfectum")
    print("6. Orqaga")
    choice = input("Tanlovingizni kiriting: ")

    if choice == "6":
        return
    print("Tanlangan operator uchun to'lov bajarilmoqda.")
    input("Ortga qaytish uchun Enter tugmasini bosing.")


def credit_payment():
    print("\nKredit to'lovlari:")
    credit_number = input("Kredit raqamini kiriting: ")
    print(f"Kredit raqami {credit_number} uchun to'lov bajarildi.")
    input("Ortga qaytish uchun Enter tugmasini bosing.")


def utility_payment():
    print("\nKomunal to'lovlar:")
    print("1. Elektr energiyasi")
    print("2. Jarimalar")
    print("3. Gaz")
    print("4. Suv")
    print("5. Orqaga")
    choice = input("Tanlovingizni kiriting: ")

    if choice == "5":
        return
    print("Tanlangan xizmat uchun to'lov bajarilmoqda.")
    input("Ortga qaytish uchun Enter tugmasini bosing.")


if __name__ == "__main__":
    print("Xush kelibsiz!")
    print("1. Uzbekcha")
    print("2. Ruscha")
    print("3. Inglizcha")
    language_choice = input("Tilni tanlang: ")
    if language_choice in ["1", "2", "3"]:
        password = input("Plastik kartangiz parolini kiriting: ")
        if password == "1234":  # Simple password check
            main_menu()
        else:
            print("Noto'g'ri parol!")
    else:
        print("Noto'g'ri tanlov!")
