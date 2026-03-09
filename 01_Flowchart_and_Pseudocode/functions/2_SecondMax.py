def SecondMax(arr):
    max1 = arr[0]
    max2 = arr[1]

    if max2 > max1:
        max1, max2 = max2, max1

    for num in arr[2:]:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num

    return max2


numbers = [3, 8, 2, 10, 5]
print(SecondMax(numbers))