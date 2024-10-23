fruits = ["apple", "banana", "cherry", "date", "elderberry"]
fruits = fruits[::-len(fruits)-1]  # Keeps elements at even indices (0, 2, ...)
print(fruits)
