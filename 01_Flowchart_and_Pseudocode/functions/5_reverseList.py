def reverseList(arr):
    length = len(arr)
    last = length - 1
    for i in range(length // 2):
        arr[i], arr[last - i] = arr[last - i], arr[i]
    return arr

arr = [1, 2, 3, 4, 5]

print(reverseList(arr))