def factorial(num):
    if num < 0:
        return None
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)

num = int(input("Enter a number to find its factorial: "))

result = factorial(num)

if result is None:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"Factorial of {num} is {result}")
