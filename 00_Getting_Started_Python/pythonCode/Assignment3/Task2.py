def factorial(n):
    if n < 0:
        return "Error : Factorial does not exist for negative numbers"
    if n == 1 or n == 0:
        return 1
    return n * factorial(n-1)


print(f"factorial of 5 is {factorial(5)}")    
print(f"factorial of 0 is {factorial(0)}")    
print(f"factorial of -3 is {factorial(-3)}")    
