input_row = int(input("row: "))
input_column = int(input("column: "))
 # Letter A
# for row in range(input_row):
#     for col in range(input_column):
#         if (
#                 (row == 0 and col != 0 and col != input_column - 1)
#                 or (col == 0 and row != 0)
#                 or (row == input_row // 2)
#                 or (row != 0 and col == input_column - 1)
#             ):
#             print("*", end="")
#         else:
#             print(end=" ")
#     print()
# print("\n\n")
# # #   Letter B
# #
# for row in range(input_row):
#     for col in range(input_column):
#         if (
#             col == 0
#             or (row == 0 and col != input_column - 1)
#             or (row == input_row - 1 and col != input_column - 1)
#             or (row == input_row // 2 and col != input_column - 1)
#             or (col == input_column - 1 and row != 0 and row != input_row // 2 and row != input_row - 1)
#         ):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# print("\n\n")
#
# # Letter D
# #
# for row in range(input_row):
#     for col in range(input_column):
#         if (
#             col == 0
#             or row == 0 and col < input_column -1
#             or (row != 0 and row != input_row - 1 and col == input_column -1 )
#             or (row == input_row - 1 and col < input_column -1)
#
#         ):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# # Letter S
# print("\n\n")
#
# for i in range(1, input_row+1):
#     for j in range(1, input_column+1):
#         if (
#
#             (i == 1)
#             or (j == 1 and i <= int(input_row//2))
#             or (i == (input_row // 2) + 1)
#             or (j == input_column  and i > input_row //2 )
#             or i == input_row
#         ):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# print("\n\n")
# # Letter E
# for row in range(input_row):
#     for col in range(input_column):
#         if (
#             col == 0
#             or (row == 0 and col != input_column - 1)
#             or (row == input_row - 1 and col != input_column - 1)
#             or (row == input_row // 2 and col != input_column - 1)
#
#         ):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#
# print("\n\n")
# # Letter F
# for row in range(input_row):
#     for col in range(input_column):
#         if (
#             col == 0
#             or (row == 0 and col != input_column - 1)
#             or (row == input_row // 2 and col != input_column - 1)
#
#         ):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# # Letter G
# print("\n\n")
# for i in range(1, input_row+1):
#     for j in range(1, input_column+1):
#         if (
#             j == 1
#             or (i == 1 and j <= input_column - 1)
#             or (i == input_row and j <= input_column - 1)
#             or (j == input_column -1 and i > input_row // 2)
#            or (j == (input_column // 2) + 1 and i == (input_row // 2) + 1)
#
#         ):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#
# # Letter H
# print("\n\n")
# for i in range(1, input_row+1):
#     for j in range(1, input_column+1):
#         if (
#             j == 1 or j == input_column or i == input_row  // 2 +1
#         ):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#
# # Letter I
# print("\n\n")
# for i in range(1, input_row+1):
#     for j in range(1, input_column+1):
#         if (
#            ( i == 1 and j != 1 and j != input_row)
#             or j == input_column // 2 + 1
#             or
#             (i == input_row and j != 1 and j != input_row)
#         ):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# letter J

# for i in range(1, input_row+1):
#     for j in range(1, input_column+1):
#         if (
#            (j != 1 and j != input_column and i == 1)
#             or (j == input_column - 1)
#             or  (j != 1 and j != input_column and i == input_row)
#             or (i == input_row - 1 and j ==  2)
#             or (i == input_row and j ==  2)
#         ):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# letter K

# rows = input_row
# cols = input_column
# for i in range(rows):
#     for j in range(cols):
#         if j == 0 or (i < rows // 2 and j == cols - 2 - i) or (i >= rows // 2 and j == i - (rows // 2)):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# print()

# Letter L
# for i in range(1, input_row+1):
#     for j in range(1, input_column+1):
#         if (
#           (j == 1 or i == input_row)
#             or (i == input_row -1 and j == input_column)
#         ):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#letter M

# for i in range(1, input_row+1):
#     for j in range(1, input_column+1):
#         if (
#          ( j == 1 or j == input_column)
#             or (i == j and j <= input_column // 2+1 and i <= input_row // 2+1)
#             or ( j == (input_column - i + 1) and i <= input_row // 2+1 )
#         ):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#

# letter N
# for i in range(1, input_row+1):
#     for j in range(1, input_column+1):
#         if (
#          ( j == 1 or j == input_column)
#             or i == j
#         ):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# letter O
# for i in range(1, input_row+1):
#     for j in range(1, input_column+1):
#         if (
#          (j == 1 and i != 1 and i != input_row)
#             or (i == 1 and j != 1 and j != input_column)
#             or ( j == input_column and i != 1 and i != input_row)
#             or (i == input_row and j != 1 and j != input_column)
#         ):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# letter P

# for i in range(1, input_row+1):
#     for j in range(1, input_column+1):
#         if (
#             j == 1
#             or (i == 1 and j != input_column)
#             or (i == input_row // 2 + 1 and j != input_column)
#             or (i == input_row // 2  and j == input_column-1)
#         ):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# letter R

# for row in range(input_row):
#     for col in range(input_column):
#         if (
#             col == 0
#             or (row == 0 and col != input_column - 1)
#             or (row == input_row // 2 and col != input_column - 1)
#             or (col == input_column - 1 and row != 0 and row != input_row // 2 and row != input_row - 1)
#             or (row == input_row -1 and col == input_column - 1)
#         ):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# print("\n\n")
# ltter Q
# for i in range(1, input_row+1):
#     for j in range(1, input_column+1):
#         if (
#          (j == 1 and i != 1 and i != input_row )
#             or (i == 1 and j != 1 and j != input_column )
#             or ( j == input_column and i != 1 and i != input_row )
#             or (i == input_row and j != 1 )
#             or (i == input_row-1 and j == input_column-1)
#             or(j == input_column and i == input_row-1)
#         ):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# Letter T

# for i in range(1, input_row+1):
#     for j in range(1, input_column+1):
#         if (
#          (i == 1 or j == input_column // 2 +1)
#
#         ):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#

# Letter U
# for i in range(1, input_row+1):
#     for j in range(1, input_column+1):
#         if (
#          (j == 1 and i != input_row)
#                 or (i == input_row and j != 1 and j != input_column)
#                 or (j == input_column and i != input_row)
#         ):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# Letter V
# for i in range(1, input_row+1):
#     for j in range(1, input_column+1):
#         if (
#              (i == j and j <= input_column // 2+1 and i <= input_row // 2+1)
#             or ( j == (input_column - i + 1) and i <= input_row // 2+1 )
#         ):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# Letter X
# for i in range(1, input_row+1):
#     for j in range(1, input_column+1):
#         if (
#              (i == j )
#             or ( j == (input_column - i + 1)  )
#         ):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# Letter z
# for i in range(1, input_row+1):
#     for j in range(1, input_column+1):
#         if (
#             i == 1 or
#              ( j == (input_column - i + 1)  )
#             or i == input_row
#         ):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# Letter Y
#
# for i in range(1, input_row+1):
#     for j in range(1, input_column+1):
#         if (
#                  (i == j and j <= input_column // 2+1 and i <= input_row // 2+1)
#                 or ( j == (input_column - i + 1)  )
#         ):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()



