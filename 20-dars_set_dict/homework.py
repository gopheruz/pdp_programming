my_set = {1, 2, 3, 4, 5, 3, 2}
unique_count = len(my_set)
print("1. Unikal elementlar soni:", unique_count)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
intersection = set1 & set2
print("2. Kesishma:", intersection)

my_set = {1, 2, 3, 4, 5}
my_set.discard(3)  
print("3. Yangilangan to'plam:", my_set)

set1 = {1, 2, 3}
set2 = {4, 5, 6}
union_set = set1 | set2
print("4. Birlashtirilgan to'plam:", union_set)

my_set = {10, 20, 5, 8, 15}
max_element = max(my_set)
min_element = min(my_set)
print("5. Eng katta element:", max_element)
print("   Eng kichik element:", min_element)

my_set = {1, 2, 3}
my_set.add(4)       
my_set.discard(2)  
print("6. Yangilangan to'plam:", my_set)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
difference = set1 - set2
print("7. Farq:", difference)

my_set = {2, 3, 4}
product = 1
for num in my_set:
    product *= num
print("8. Ko'paytma:", product)

my_set = set()
is_empty = len(my_set) == 0
print("9. To'plam bo'shmi?", is_empty)

my_set = {1, 2, 3, 4, 5}
length = len(my_set)
print("10. To'plam uzunligi:", length)
