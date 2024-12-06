def reverse_list(lstData):
    data = []
    start = len(lstData)-1
    while start >= 0:
        data.append(lstData[start])
        start -= 1
    return data


teslist = [1,2,3,4,5,6,7,8,9]

print(reverse_list(teslist))