# Greatest Common Divisor (GCD) & Least Common Multiple (LCM)

Greatest Common Divisor (GCD) and Least Common Multiple (LCM) are cornerstones of number theory and competitive programming. This document covers basic concepts, mathematical proofs, optimized algorithms, and advanced applications like the Extended Euclidean Algorithm.

---

## 1️⃣ Greatest Common Divisor (GCD)

### Problem Statement
Given two positive integers $a$ and $b$, find their Greatest Common Divisor (GCD), which is the largest positive integer that divides both $a$ and $b$ without leaving a remainder.

### Examples
```text
Input:  a = 12, b = 18
Output: 6
Explanation: Divisors of 12 are 1, 2, 3, 4, 6, 12. Divisors of 18 are 1, 2, 3, 6, 9, 18. Common divisors are 1, 2, 3, 6. The largest is 6.

Input:  a = 17, b = 23
Output: 1
Explanation: Both are prime numbers, so their only common divisor is 1.
```

---

## 2️⃣ The Euclidean Algorithm (Subtraction Method)

### Concept
The Euclidean algorithm is based on the principle that the GCD of two numbers also divides their difference. Specifically:
$$\text{GCD}(a, b) = \text{GCD}(a - b, b) \quad (\text{if } a > b)$$

### Python Code (Subtraction Method)
```python
def gcd_subtraction(a: int, b: int) -> int:
    """
    Computes GCD of two numbers using repeated subtraction.
    """
    if a == 0:
        return b
    if b == 0:
        return a
        
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a
```

### Complexity Analysis
* **Time Complexity**: $O(\max(a, b))$ in the worst case (e.g., $a = 10^9$ and $b = 1$, which requires $10^9$ subtractions).
* **Space Complexity**: $O(1)$ auxiliary space.

---

## 3️⃣ Optimized Euclidean Algorithm (Division Method)

### Concept
Instead of subtracting repeatedly, we can divide the larger number by the smaller number and take the remainder using the modulo operator (`%`):
$$\text{GCD}(a, b) = \text{GCD}(b, a \bmod b)$$
This reduces the numbers much faster. The algorithm terminates when the remainder becomes `0`, and the last non-zero value is the GCD.

### Python Code (Recursive)
```python
def gcd_recursive(a: int, b: int) -> int:
    """
    Computes GCD recursively using modulo division.
    """
    return a if b == 0 else gcd_recursive(b, a % b)
```

### Python Code (Iterative)
```python
def gcd_iterative(a: int, b: int) -> int:
    """
    Computes GCD iteratively using modulo division.
    """
    while b > 0:
        a, b = b, a % b
    return a
```

### Built-in Python Implementation
Python's standard library provides a built-in optimized function for calculating the GCD:
```python
import math
ans = math.gcd(a, b)
```

### Time Complexity Analysis
* **Time Complexity**: $O(\log(\min(a, b)))$
  * **Proof (Lamé's Theorem)**: The number of division steps is at most 5 times the number of digits in the smaller number.
  * **Worst-Case Scenario**: The worst-case inputs are consecutive Fibonacci numbers (e.g., $F_n$ and $F_{n-1}$), as they produce a remainder sequence consisting of smaller Fibonacci numbers, requiring the maximum number of steps.
* **Space Complexity**:
  * **Iterative**: $O(1)$
  * **Recursive**: $O(\log(\min(a, b)))$ due to the recursion call stack.

---

## 4️⃣ Least Common Multiple (LCM)

### Concept & Formula
The **Least Common Multiple** (LCM) of two integers $a$ and $b$ is the smallest positive integer that is divisible by both $a$ and $b$.

There is a fundamental relationship between GCD and LCM:
$$a \times b = \text{GCD}(a, b) \times \text{LCM}(a, b)$$

From this, we derive the formula for LCM:
$$\text{LCM}(a, b) = \frac{|a \times b|}{\text{GCD}(a, b)}$$

> [!IMPORTANT]
> **Implementation Tip**: To prevent integer overflow in languages with fixed-width integers (and for performance optimization in Python), perform division *before* multiplication:
> `lcm = (a // gcd(a, b)) * b`

### Python Code
```python
def lcm(a: int, b: int) -> int:
    """
    Computes the Least Common Multiple (LCM) using GCD.
    """
    if a == 0 or b == 0:
        return 0
    return (abs(a) // gcd_iterative(a, b)) * abs(b)
```

### Built-in Python Implementation
From Python 3.9+, the `math` module has a built-in LCM function:
```python
import math
ans = math.lcm(a, b)
```

### Complexity Analysis
* **Time Complexity**: $O(\log(\min(a, b)))$ (dominated by the GCD computation).
* **Space Complexity**: $O(1)$.

---

## 5️⃣ Extended Euclidean Algorithm

### Concept & Bézout's Identity
The standard Euclidean algorithm only finds the GCD. The **Extended Euclidean Algorithm** also finds integer coefficients $x$ and $y$ such that:
$$a \cdot x + b \cdot y = \text{GCD}(a, b)$$
This is known as **Bézout's Identity**. The coefficients $x$ and $y$ can be computed by tracking the quotients at each step of the division method and working backwards.

### Derivation
For recursive step:
$$\text{GCD}(a, b) = \text{GCD}(b, a \bmod b)$$
Suppose we have coefficients $x_1$ and $y_1$ for the step $(b, a \bmod b)$:
$$b \cdot x_1 + (a \bmod b) \cdot y_1 = g$$
Since $a \bmod b = a - \lfloor \frac{a}{b} \rfloor \cdot b$, we substitute this back:
$$b \cdot x_1 + \left(a - \lfloor \frac{a}{b} \rfloor \cdot b\right) \cdot y_1 = g$$
$$a \cdot y_1 + b \cdot \left(x_1 - \lfloor \frac{a}{b} \rfloor \cdot y_1\right) = g$$
Comparing this with $a \cdot x + b \cdot y = g$, we get:
$$x = y_1$$
$$y = x_1 - \lfloor \frac{a}{b} \rfloor \cdot y_1$$

### Python Code
```python
def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    """
    Computes GCD and coefficients x, y for Bézout's Identity:
    a * x + b * y = gcd(a, b)
    
    Returns:
        (gcd, x, y)
    """
    if b == 0:
        return a, 1, 0
    
    gcd, x1, y1 = extended_gcd(b, a % b)
    
    # Update x and y using the recurrence relation
    x = y1
    y = x1 - (a // b) * y1
    
    return gcd, x, y

# Example Usage
gcd_val, x, y = extended_gcd(30, 20)
print(f"GCD: {gcd_val}, x: {x}, y: {y}")
# Output: GCD: 10, x: 1, y: -1 (Since 30*(1) + 20*(-1) = 10)
```

### Applications of Extended Euclidean Algorithm
1. **Modular Multiplicative Inverse**:
   If we want to find $x$ such that $a \cdot x \equiv 1 \pmod m$, we solve $a \cdot x + m \cdot y = 1$. This has a solution if and only if $\text{GCD}(a, m) = 1$ (coprime).
   ```python
   def mod_inverse(a: int, m: int) -> int:
       gcd, x, _ = extended_gcd(a, m)
       if gcd != 1:
           raise ValueError("Inverse does not exist (not coprime)")
       return (x % m + m) % m
   ```
2. **Solving Linear Diophantine Equations**:
   Equations of the form $a \cdot x + b \cdot y = c$ have integer solutions if and only if $c$ is a multiple of $\text{GCD}(a, b)$.

---

## 6️⃣ GCD and LCM of Multiple Numbers

### GCD of an Array
To find the GCD of an array of numbers, we can recursively apply the two-number GCD:
$$\text{GCD}(a_1, a_2, \dots, a_n) = \text{GCD}(a_1, \text{GCD}(a_2, \dots, a_n))$$

### LCM of an Array
Similarly, the LCM of an array is:
$$\text{LCM}(a_1, a_2, \dots, a_n) = \text{LCM}(a_1, \text{LCM}(a_2, \dots, a_n))$$

### Python Code
```python
from functools import reduce

def gcd_multiple(nums: list[int]) -> int:
    """
    Computes the GCD of a list of numbers.
    """
    return reduce(gcd_iterative, nums)

def lcm_multiple(nums: list[int]) -> int:
    """
    Computes the LCM of a list of numbers.
    """
    return reduce(lcm, nums)
```

---

## 7️⃣ Essential Interview Problems

### 1. Simplify Fractions
* **Problem**: Given a fraction represented by numerator and denominator, simplify it to its reduced form.
* **Approach**: Divide both numerator and denominator by their GCD.

### 2. LeetCode 365: Water Jug Problem
* **Problem**: You are given two jugs of capacity $x$ and $y$ liters. Can you measure exactly $z$ liters?
* **Approach**: By Bézout's identity, you can measure $z$ liters if and only if $z$ is a multiple of $\text{GCD}(x, y)$ and $z \le x + y$.

### 3. LeetCode 914: X of a Kind in a Deck of Cards
* **Problem**: Check if you can partition the cards into groups of size $X \ge 2$ containing the same value.
* **Approach**: Compute the frequency of each card type and find the overall GCD of the frequencies. If the GCD $\ge 2$, return `True`.