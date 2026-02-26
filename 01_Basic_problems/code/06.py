def least_common_multiple(a, b):
    def gcd(x, y):
        while y != 0:
            x, y = y, x % y
        return x

    return abs(a * b) // gcd(a, b)

print(least_common_multiple(4, 6))  # Output: 12
print(least_common_multiple(15, 20))  # Output: 60
print(least_common_multiple(3, 5))  # Output: 15