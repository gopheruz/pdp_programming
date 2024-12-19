import Write_data as cardSecurity

def PayforPhone():
    amount = int(cardSecurity.inputValue("summa"))
    return  cardSecurity.minus_amount(minus_amount=amount)

def Ucell():
    phon_number = cardSecurity.inputValue("telefon raqam")
    while phon_number[4:7] not in ["50", "93", "94"]:
            print("xato raqam ucell 50, 93, 94")
            phon_number = cardSecurity.inputValue("telefon raqam")
    payment_sucsedd = PayforPhone()
    return phon_number, payment_sucsedd

def Beeline():
    phon_number = cardSecurity.inputValue("telefon raqam")
    while phon_number[4:7] not in ["90", "91"]:
            print(f"xato raqam Beeline {["90", "91"]}")
            phon_number = cardSecurity.inputValue("telefon raqam")
    payment_sucsedd = PayforPhone()
    return phon_number, payment_sucsedd

def Uzmobile():
    phon_number = cardSecurity.inputValue("telefon raqam")
    while phon_number[4:7] not in ["77", "99", "95"]:
            print("xato raqam Uzmobile 77, 99, 95")
            phon_number = cardSecurity.inputValue("telefon raqam")
    payment_sucsedd = PayforPhone()
    return phon_number, payment_sucsedd

def MobiUz():
    phon_number = cardSecurity.inputValue("telefon raqam")
    while phon_number[4:7] not in ["88", "97"]:
            print("xato raqam mobiuz 88, 97, 98")
            phon_number = cardSecurity.inputValue("telefon raqam")
    payment_sucsedd = PayforPhone()
    return phon_number, payment_sucsedd

def Perfectum():
    phon_number = cardSecurity.inputValue("telefon raqam")
    while phon_number[4:7] != "98":
            print("xato raqam only 98")
            phon_number = cardSecurity.inputValue("telefon raqam")
    payment_sucsedd = PayforPhone()
    return phon_number, payment_sucsedd
