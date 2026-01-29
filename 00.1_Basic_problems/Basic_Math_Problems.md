

# Mathematical Problems (DSA – Python)

Mathematical problems form the **foundation of Data Structures and Algorithms**.
They improve **logical thinking, loop control, condition handling, and number manipulation**, which are critical for cracking **Google, Amazon, Microsoft** interviews.

---

## 1️⃣ Count Number of Digits in a Number

### Problem Statement

User will get number using input `N`, you have to count how many digits it contains.

### Example

```
Input:  N = 4567
Output: 4
```

### Approach

* Repeatedly divide the number by 10.
* Increment a counter until the number becomes 0.

### Python Code

```python
def countNum():
    count = 0

    x = int(input("Enter a number: "))
    while x > 0:
        count += 1
        x //= 10
    return count

print(r"Your number have ", countNum(), " digits.")
```

### Time Complexity

* **O(log₁₀ N)**
  Each division by 10 removes one digit.

### Space Complexity

* **O(1)**
  Only a constant number of variables are used.

---

## 2️⃣ Reverse a Number

### Problem Statement

Given an integer `N`, reverse its digits.

### Example

```
Input:  N = 1234
Output: 4321
```

### Approach

* Extract the last digit using `% 10`
* Build the reversed number using multiplication

### Python Code

```python
def reverse_number(n):
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    return reversed_num

print(reverse_number(12345))
```

### Time Complexity

* **O(log₁₀ N)**

### Space Complexity

* **O(1)**

---

## 3️⃣ Check Palindrome Number

### Problem Statement

Check whether a number is a palindrome or not.

### Example

```
Input:  N = 121
Output: True
```

### Approach

* Reverse the number
* Compare with the original number

### Python Code 1

```python
def is_palindrome(n):
    original = n
    reverse = 0

    while n > 0:
        reverse = reverse * 10 + n % 10
        n //= 10

    return original == reverse

### Time Complexity 
O(log₁₀ N)

### Space Complexity
O(1)
```



### Python Code 2

```python
def isPalindrome(self, s: str) -> bool:
        st = ''.join(ch.lower() for ch in s if ch.isalnum())
        left = 0
        right = len(st) - 1

        while left < right:
            if st[left] != st[right]:
                return False
            left += 1
            right -= 1
        return True
```
### Python Code 3

```python
import re
def isPalindrome(s: str) -> bool:
        cleaned_st = re.sub(r'[^a-zA-Z0-9]', '', s)
        return cleaned_st.lower() == cleaned_st[::-1].lower()

print(isPalindrome("A man, a plan, a canal: Panama"))
```

---

## 4️⃣ Check Prime Number

### Problem Statement

Check whether a number `N` is prime.

### Example

```
Input:  N = 29
Output: True
```

### Optimized Approach

* Check divisibility only up to `√N`
* Skip unnecessary checks

### Python Code

```python
import math

class Solution:
    def isPrime(self, n: int):
        if n <= 1:
            return False
        for i in range(2, int( math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def countPrimes(self, n: int) -> int:
        primeNums = []
        for num in range(n + 1):
            if self.isPrime(num):
                primeNums.append(num)
        return len(primeNums)

# LeetCode 204
Sieve ka idea samjho
```

### Time Complexity

* **O(N√N)**

### Space Complexity

* **O(1)**

---

## 5️⃣ Find GCD (Greatest Common Divisor)

### Problem Statement

Find the GCD of two numbers using **Euclidean Algorithm**.

### Example

```
Input:  a = 36, b = 24
Output: 12
```

### Approach (Euclidean Algorithm)

* GCD(a, b) = GCD(b, a % b)
* Continue until `b = 0`

### Python Code

```python
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
```

### Time Complexity

* **O(log min(a, b))**

### Space Complexity

* **O(1)**

---

## 6️⃣ Find LCM (Least Common Multiple)

### Formula Used

```
LCM(a, b) = (a × b) / GCD(a, b)
```

### Python Code

```python
def lcm(a, b):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    return (a * b) // gcd(a, b)
```

### Time Complexity

* **O(log min(a, b))**

### Space Complexity

* **O(1)**

---

## 7️⃣ Factorial of a Number

### Problem Statement

Find factorial of a number `N`.

### Example

```
Input:  N = 5
Output: 120
```

### Python Code

```python
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
```

### Time Complexity

* **O(N)**

### Space Complexity

* **O(1)**

---

## 8️⃣ Fibonacci Number (Nth Term)

### Problem Statement

Find the `N`th Fibonacci number.

### Optimized Iterative Approach

### Python Code

```python
def fibonacci(n):
    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
```

### Time Complexity

* **O(N)**

### Space Complexity

* **O(1)**

---

## 9️⃣ Armstrong Number

### Problem Statement

Check whether a number is an Armstrong number.

### Example

```
Input:  N = 153
Output: True
```

### Python Code

```python
def is_armstrong(n):
    digits = len(str(n))
    temp = n
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    return total == n
```

### Time Complexity

* **O(log₁₀ N)**

### Space Complexity

* **O(1)**