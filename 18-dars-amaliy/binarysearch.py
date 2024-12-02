def binary_search(lst, item):
    low = 0
    high = len(lst) - 1
    count = 0
    while low <= high:
        count += 1
        mid = (low + high) // 2
        if lst[mid] == item:
            print(f"count {count}")
            return mid
        elif lst[mid] < item:
            low = mid + 1
        else:
            high = mid - 1
print(binary_search([i for i in range(100)], 7))