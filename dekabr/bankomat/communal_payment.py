import Write_data as cardSecurity
def electricity_payment():
    amount = int(cardSecurity.inputValue("elekter energiya to'lovi"))
    return cardSecurity.minus_amount(minus_amount=amount)

def penaltiy():
    amount = int(cardSecurity.inputValue("jarima to'lovi"))
    return cardSecurity.minus_amount(minus_amount=amount)
def gas():
    amount = int(cardSecurity.inputValue("gaz to'lovi"))
    return cardSecurity.minus_amount(minus_amount=amount)
def water():
    amount = int(cardSecurity.inputValue("suv to'lovi"))
    return cardSecurity.minus_amount(minus_amount=amount)
