def removeDuplicate(arr):
    unique_arr = []
    for num in arr:
        if num not in unique_arr:
            unique_arr.append(num)
    return unique_arr

arr = [1, 2, 2, 3, 4, 4, 5]
print(removeDuplicate(arr))