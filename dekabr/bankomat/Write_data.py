def get_current_money(filename="money.txt"):
    with open(filename, 'r') as file:
        for line in file:
            if "defaultmoney=" in line:
                return int(line.strip().split('=')[1]) 
    return 0


def add_amount(filename="money.txt", added_amount=0):
    current_money = get_current_money(filename)
    new_money = current_money + added_amount
    with open(filename, 'w') as file:
        file.write(f"defaultmoney={new_money}")


def minus_amount(filename="money.txt", minus_amount=0):
    current_money = get_current_money(filename)
    if current_money >= minus_amount:
        new_money = current_money - minus_amount
        with open(filename, 'w') as file:
            file.write(f"defaultmoney={new_money}")
        return True  
    return False


def Howmanyto(amount):
    return amount-get_current_money()
def GetPassword(filename="password.txt"):
    with open(filename, "r") as passwordfile:
        for i in passwordfile:
            return i.split("=")[1]
        

def Change_password(oldPassword, newPassword1, newpassword2, filename="password.txt"):
    if GetPassword(filename) == oldPassword and newPassword1 == newpassword2:
        with open(filename, "w") as passwordFile:
            passwordFile.write(f"password={newPassword1}")
            return True
    return False

def checkPin(pin):
    return pin == GetPassword()

def inputValue(value):
    result = input(f"{value}ni kiriting: ")
    return result