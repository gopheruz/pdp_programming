pattern =""
n = 12
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

print(pattern)