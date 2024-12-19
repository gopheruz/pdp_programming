


# sanoq = 0
number = 123
# while number > 0:
#     sanoq +=1
#     number //=10
# print(sanoq)


# count = 0
# def counterfunc(a):
#     global count
#     if a < 0:
#         a = a * -1
#     if a == 0 and count == 0:
#         count = 1
#     elif a > 0:
#         count += 1
#         counterfunc(a // 10)
#     return count

def CountNumbber(x):
    if x < 0:
        x = -x
    if x < 10:
        return 1
    return 1 + CountNumbber(x // 10)

print(CountNumbber(-1234))

