def is_armstrong(n):
    digits = len(str(n))
    temp = n
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    return total == n

print(is_armstrong(153))  # Example usage: check if 153 is an Armstrong number