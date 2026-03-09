def MaxInList(arr):
    max = arr[0]
    for i in arr:
        if i > max:
            max = i
    return max


numbers = [3, 8, 2, 10, 5]
Max = MaxInList(numbers)
print(Max)