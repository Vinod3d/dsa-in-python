def countNum():
    count = 0

    x = int(input("Enter a number: "))
    while x > 0:
        count += 1
        x //= 10
    return count

print(r"Your number have ", countNum(), " digits.")  # Example usage