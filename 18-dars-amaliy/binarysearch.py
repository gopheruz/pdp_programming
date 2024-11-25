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
print(binary_search([1,2,3,4,5,6,7,8,9], 7))