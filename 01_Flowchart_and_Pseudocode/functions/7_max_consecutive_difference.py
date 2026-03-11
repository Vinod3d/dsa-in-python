def max_consecutive_difference(arr):
    if len(arr) < 2:
        return 0
    max_diff = 0
    for i in range(1, len(arr)):
        diff = abs(arr[i] - arr[i - 1])
        if diff > max_diff:
            max_diff = diff
    return max_diff

arr = [1, 7, 3, 10, 5]

print(max_consecutive_difference(arr))