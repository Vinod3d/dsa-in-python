# print fibonacci series up to n terms
def fibonacci(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

print(fibonacci(10))  # Example usage: print first 10 terms of Fibonacci series