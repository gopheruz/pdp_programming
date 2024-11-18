# for i in range(-99, 100):
#     if i < 10 and i > -10:
#         continue
#     print(i)

# i = 1
# while i <= 10:
#     if i == 5:
#         i += 1
#         continue
#     print(i)
#     i += 1


# array = [1,2,3,4,5,6,7,8,9,0]
# has = False
# for i in array:
#     if i == 7:
#         has = True
#         break

# if has:
#     print("bor")
# else:
#     print("yo'q")


# son  =  int(input(("son kiriting: ")))
# counter = 0
# isprime = True
# for i in range(1, son + 1):
#     if son % i == 0:
#         counter += 1
#         if counter > 2:
#             isprime = False
#             break
# if isprime:
#     print("Tub son")
# else:
#     print("Murakkab son")

a = 0
b = 1
next = a + b

n = int(input("n: "))

while next < n:
    print(next)
    a = b
    b = next
    next = a + b