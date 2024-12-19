# def summa(s, f):
#     if s <= f:
#         return s * summa(s+1, f)
#     return 1
#
# print(summa(1, 5))


#
# summa(1, 10)
#  └── 1 + summa(2, 10)
#       └── 2 + summa(3, 10)
#            └── 3 + summa(4, 10)
#                 └── 4 + summa(5, 10)
#                      └── 5 + summa(6, 10)
#                           └── 6 + summa(7, 10)
#                                └── 7 + summa(8, 10)
#                                     └── 8 + summa(9, 10)
#                                          └── 9 + summa(10, 10)
#                                               └── 10 + summa(11, 10)
#                                                    └── 0 (Base Case)


# def summa(n):
#     if n == 0:
#         return 0
#     return n % 10 + summa(n // 10)
#
# print(summa(125))

def sanoq(a = 10):
    if a > 0:
        sanoq(a -1)
        print(a)

sanoq()