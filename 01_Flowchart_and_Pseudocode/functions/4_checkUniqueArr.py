def checkUniqueArr(arr):
    for i, num in enumerate(arr):
        if num in arr[i+1:]:
            return False
    return True

# arr = [1, 2, 2, 3, 4, 4, 5]
arr = [1, 2, 3, 4, 5]

print(checkUniqueArr(arr))