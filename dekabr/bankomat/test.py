mylist =  (('apple', 'banana', 'cherry'))
print(mylist) 
list2 = list(mylist)
print(list2)
for i in range(len(list2)):
    list2[i] = list2[i].capitalize()

print(list2)