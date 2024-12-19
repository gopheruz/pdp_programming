import Write_data as cardSecurity
def payforCredit():
    creditNumber = cardSecurity.inputValue("credit raqami")
    amount = int(cardSecurity.inputValue("summa"))
    return (creditNumber, cardSecurity.minus_amount(minus_amount=amount))
