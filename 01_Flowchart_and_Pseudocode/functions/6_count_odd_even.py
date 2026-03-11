def count_odd_even(arr):
    odd_count = 0
    even_count = 0
    for num in arr:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count

arr = [1, 2, 3, 4, 5]

print(count_odd_even(arr))