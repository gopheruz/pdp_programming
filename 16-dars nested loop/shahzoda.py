input_row = int(input("row: "))
input_column = int(input("col: "))
letters = []  
name = ""
for i in range(1, input_row + 1):
    for j in range(1, input_column + 1):
        if (
            i == 1
            or (j == 1 and i <= input_row // 2)
            or i == (input_row // 2) + 1
            or (j == input_column and i > input_row // 2)
            or i == input_row
        ):
            name += "❤️ "
        else:
            name += "  "
    name += "\n"
letters.append(name)

name = ""
for i in range(1, input_row + 1):
    for j in range(1, input_column + 1):
        if j == 1 or j == input_column or i == input_row // 2 + 1:
            name += "❤️ "
        else:
            name += "  "
    name += "\n"
letters.append(name)


name = ""
for row in range(input_row):
    for col in range(input_column):
        if (
            (row == 0 and col != 0 and col != input_column - 1)
            or (col == 0 and row != 0)
            or (row == input_row // 2)
            or (row != 0 and col == input_column - 1)
        ):
            name += "❤️ "
        else:
            name += "  "
    name += "\n"
letters.append(name)
name = ""
for i in range(1, input_row + 1):
    for j in range(1, input_column + 1):
        if j == 1 or j == input_column or i == input_row // 2 + 1:
            name += "❤️ "
        else:
            name += "  "
    name += "\n"
letters.append(name)
name = ""
for i in range(1, input_row + 1):
    for j in range(1, input_column + 1):
        if i == 1 or (j == input_column - i + 1) or i == input_row:
            name += "❤️ "
        else:
            name += "  "
    name += "\n"
letters.append(name)

name = ""
for i in range(1, input_row + 1):
    for j in range(1, input_column + 1):
        if i == 1 or j == 1 or i == input_row or j == input_column:
            name += "❤️ "
        else:
            name += "  "
    name += "\n"
letters.append(name)

name = ""
for row in range(input_row):
    for col in range(input_column):
        if (
            col == 0
            or (row == 0 and col < input_column - 1)
            or (row != 0 and row != input_row - 1 and col == input_column - 1)
            or (row == input_row - 1 and col < input_column - 1)
        ):
            name += "❤️ "
        else:
            name += "  "
    name += "\n"
letters.append(name)

name = ""
for row in range(input_row):
    for col in range(input_column):
        if (
            (row == 0 and col != 0 and col != input_column - 1)
            or (col == 0 and row != 0)
            or (row == input_row // 2)
            or (row != 0 and col == input_column - 1)
        ):
            name += "❤️ "
        else:
            name += "  "
    name += "\n"
letters.append(name)

n = 10
pattern = ""

for i in range(n // 2, n, 2):
    for j in range(1, n - i, 2):
        pattern += " "

    for j in range(1, i + 1):
        pattern += "*"

    for j in range(1, n - i + 1):
        pattern += " "

    for j in range(1, i + 1):
        pattern += "*"
    
    pattern += "\n"

for i in range(n, 0, -1):
    for j in range(0, n - i):
        pattern += " "
    
    for j in range(1, i * 2):
        pattern += "*"
    
    pattern += "\n"

letters.append(pattern)
final_output = ""
for lines in zip(*[letter.splitlines() for letter in letters]):
    final_output += "   ".join(lines) + "\n"
print(final_output)