nested_tuple = (1, 2, (3, 4, 5), 6, 7)
print(nested_tuple[2][1])
for i in (nested_tuple):
    if isinstance(i, tuple):
        for j in (i):
            print(j)
    else:
        print(i)

_salom = "salom"

print(_salom)   