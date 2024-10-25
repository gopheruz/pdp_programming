name = input("talaba ismi: ")
age = int(input("talaba yoshi: "))
ball = int(input("talaba bali: "))
tolaganKontrakti = int(input("talab qancha kontrakt to'lagan: "))
kontraktsummasu = int(input("Kontrakt summasi: "))

check = age > 17 and ball > 50 and (kontraktsummasu / 2) >= tolaganKontrakti
print(check)