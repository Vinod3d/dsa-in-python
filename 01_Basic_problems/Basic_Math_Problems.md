

# Mathematical Problems (DSA – Python)

Mathematical problems form the **foundation of Data Structures and Algorithms**.
They improve **logical thinking, loop control, condition handling, and number manipulation**, which are critical for cracking **Google, Amazon, Microsoft** interviews.

---

## 1️⃣ Count Number of Digits in a Number

#### Problem Statement

User will get number using input `N`, you have to count how many digits it contains.

#### Example

```
Input:  N = 4567
Output: 4
```

#### Approach

* Repeatedly divide the number by 10.
* Increment a counter until the number becomes 0.

#### Python Code

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

#### Time Complexity

* **O(log₁₀ N)**
  Each division by 10 removes one digit.

#### Space Complexity

* **O(1)**
  Only a constant number of variables are used.

---

## 2️⃣ Reverse a Number

#### Problem Statement

Given an integer `N`, reverse its digits.

#### Example

```
Input:  N = 1234
Output: 4321
```

#### Approach

* Extract the last digit using `% 10`
* Build the reversed number using multiplication

#### Python Code

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

#### Time Complexity

* **O(log₁₀ N)**

#### Space Complexity

* **O(1)**

---

## 3️⃣ Check Palindrome Number

#### Problem Statement

Check whether a number is a palindrome or not.

#### Example

```
Input:  N = 121
Output: True
```

#### Approach

* Reverse the number
* Compare with the original number

#### Python Code 1

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

#### Problem Statement

Check whether a number `N` is prime.

#### Example

```
Input:  N = 29
Output: True
```

#### Optimized Approach

* Check divisibility only up to `√N`
* Skip unnecessary checks

#### Python Code

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

#### Time Complexity

* **O(N√N)**

#### Space Complexity

* **O(1)**

---

## 5️⃣ Find GCD (Greatest Common Divisor)

#### Problem Statement

Find the GCD of two numbers using **Euclidean Algorithm**.

#### Example

```
Input:  a = 36, b = 24
Output: 12
```

#### Approach (Euclidean Algorithm)

* GCD(a, b) = GCD(b, a % b)
* Continue until `b = 0`

#### Python Code 1

```python
def gcd(a, b):
    ans = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            ans = i
    return ans

print(gcd(18, 36))
```
#### Python Code 2

```python
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
    
print(gcd(18, 36))
```

#### Time Complexity

* **O(log min(a, b))**

#### Space Complexity

* **O(1)**

---

## 6️⃣ Find LCM (Least Common Multiple)

#### Formula Used

```
LCM(a, b) = (a × b) / GCD(a, b)
```

#### Python Code

```python
def least_common_multiple(a, b):
    def gcd(x, y):
        while y != 0:
            x, y = y, x % y
        return x

    return abs(a * b) // gcd(a, b)

print(least_common_multiple(4, 6))  # Output: 12
print(least_common_multiple(15, 20))  # Output: 60
print(least_common_multiple(3, 5))  # Output: 15
```

#### Time Complexity

* **O(log min(a, b))**

#### Space Complexity

* **O(1)**

---
## 7️⃣ Convert Number to Roman


#### Python Code

```python
def intToRoman(num: int) -> str:
        values = [
            (1000, "M"),
            (900,  "CM"),
            (500,  "D"),
            (400,  "CD"),
            (100,  "C"),
            (90,   "XC"),
            (50,   "L"),
            (40,   "XL"),
            (10,   "X"),
            (9,    "IX"),
            (5,    "V"),
            (4,    "IV"),
            (1,    "I")
        ]

        res = []
        for val, sym in values:
            while num >= val:
                num -= val
                res.append(sym)
        return "".join(res)

print(intToRoman(3999)) # Output: "MMMCMXCIX"
```

#### Time Complexity
values list fixed size (13 symbols) ki hai

* **O(1)**

#### Space Complexity

* **O(1)**

---
## 8️⃣ Convert Roman to Number

#### Python Code

```python
def romanToInt(s: str) -> int:
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0

        for i in range(len(s)):
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                total -= roman[s[i]]
            else:
                total += roman[s[i]]

        return total
print(romanToInt("MMMMDLXXII"))
```

#### Time Complexity

* **O(n)**

#### Space Complexity

* **O(1)**

---

## 9️⃣ Factorial of a Number

#### Problem Statement

Find factorial of a number `N`.

#### Example

```
Input:  N = 5
Output: 120
```

#### Python Code

```python
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

```

#### Time Complexity

* **O(N)**

#### Space Complexity

* **O(1)**

---

## 1️⃣0️⃣ Fibonacci Number (Nth Term)

#### Problem Statement

Find the `N`th Fibonacci number.

#### Optimized Iterative Approach

#### Python Code

```python
def fibonacci(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

print(fibonacci(10))

# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

#### Time Complexity

* **O(N)**

#### Space Complexity

* **O(1)**

---

## 1️⃣1️⃣ Armstrong Number

#### Problem Statement

Check whether a number is an Armstrong number.

#### Example

```
Input:  N = 153
Output: True
```

#### Python Code

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

#### Time Complexity

* **O(log₁₀ N)**

#### Space Complexity

* **O(1)**
## 1️⃣2️⃣ Check Is Trionic Array

#### Problem Statement

You are given an integer array nums of length n.

An array is called trionic if there exist indices
0 < p < q < n − 1 such that:

nums[0…p] is strictly increasing

nums[p…q] is strictly decreasing

nums[q…n−1] is strictly increasing

#### Example

```
Input:  nums = [1, 3, 5, 4, 2, 6]
Output: True
```


#### Python Code

```python
def isTrionic( nums: List[int]) -> bool:
        n = len(nums)
        if n <4:
            return False
        phase = 0
        inc = 0

        for i in range(1, n):
            if nums[i] == nums[i-1]:
                return False
            
            if phase == 0:
                if nums[i] > nums[i - 1]:
                    inc+=1
                else:
                    if inc == 0:
                        return False
                    phase = 1
            
            elif phase == 1:
                if nums[i] > nums[i - 1]:
                    phase = 2
            else:
                if nums[i] < nums[i - 1]:
                    return False
        return phase == 2

# print(isTrionic([1, 3, 2, 4, 3]))  # Output: False
print(isTrionic([1, 3, 5, 4, 2, 6]))  
```

#### Time Complexity

* **O(N)**

#### Space Complexity

* **O(1)**