import math
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# print(isPrime(29))  # Example usage

# Print all prime numbers in a given range
def primesInRange(start, end):
    primes = []
    for num in range(start, end + 1):
        if isPrime(num):
            primes.append(num)
    return primes

print(primesInRange(10, 50))  # Example usage