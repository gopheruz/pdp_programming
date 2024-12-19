## function with named parametrs


# def InfoPerson(name ,age):
#     print(f"Hello {name}")
#     print(f"I am {age} years old")
#
# ism = input("name: ")
# yoshi = int(input("age: "))
#
# InfoPerson(ism,yoshi)
# InfoPerson(age=yoshi, name=ism)


##

def Element(toplam, x):
    newlst = []
    for i in toplam:
        if i > x:
            newlst.append(i)
    return newlst

lst = [1,2,3,5,6,7,8,34,23,12,434,5]

print(Element(lst, 50))