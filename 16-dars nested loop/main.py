# llst = ["Dushanba", "Seshanba","Chorchanba", "Payshanba", "Juma", "Shanba", "Yakshanba"]
# for i in range(1, 5):
#     print(f"{i}-hafta")
#     for j in range(7):
#         print(f"\t{llst[j]}")

import time
row = int(input("r: "))
column = int(input("c: "))
ortaRow = row // 2
mid = column // 2
print(ortaRow, mid)
for i in range(row):
    for j in range(column):
        if (
                i == 0 and mid - 1 <= j <= mid + 1 or
                j == mid - i or j == mid + i or
                i == row // 2
        ):
            print("*", end="")
        else:
            print(f" ", end="")
    time.sleep(.5)
    print()