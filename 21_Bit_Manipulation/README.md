# 21. Bit Manipulation 🔌

Bit Manipulation is a technique where we work directly with the **binary digits (bits)** of a number. Instead of doing standard math like adding or multiplying, we modify the `0`s and `1`s directly.

Since computers store everything as bits, bitwise operations are **incredibly fast** (they take just 1 CPU cycle). Mastering this topic will give you a major advantage in coding interviews at companies like Google, Meta, and Amazon.

---
### 1️⃣ Types of bases

| Base | Name | Digits Used | Powers | Example |
| :--- | :--- | :--- | :--- | :--- |
| 2 | **Binary** | 0, 1 | $2^0, 2^1, 2^2, ...$ | `1101` (13) |
| 8 | **Octal** | 0–7 | $8^0, 8^1, 8^2, ...$ | `15` (13) |
| 10 | **Decimal** | 0–9 | $10^0, 10^1, 10^2, ...$ | `13` (13) |
| 16 | **Hexadecimal** | 0–9, A–F | $16^0, 16^1, 16^2, ...$ | `D` (13) |

### 2️⃣ Bitwise Operators

| Operator | Name | Description | Example | Result |
| :--- | :--- | :--- | :--- | :--- |
| `&` | **AND** | Returns 1 if both bits are 1. | `1 & 1 = 1`, `1 & 0 = 0` | `1` |
| `pipe` | **OR** | Returns 1 if at least one bit is 1. | `1 pipe 0 = 1`, `0 pipe  0 = 0` | `1` |
| `^` | **XOR** | Returns 1 if bits are different. | `1 ^ 0 = 1`, `1 ^ 1 = 0` | `1` |
| `~` | **NOT** | Flips the bit. | `~1 = 0`, `~0 = 1` | `0` |
| `<<` | **Left Shift** | Shifts bits to the left, filling with 0s. | `5 << 1 = 10` | `10` |
| `>>` | **Right Shift** | Shifts bits to the right. | `5 >> 1 = 2` | `2` |

### 3️⃣ Understanding Binary (Base 2)

Our daily number system is **Base 10 (Decimal)**. It uses ten digits (0 to 9). The value of a digit is based on powers of 10.
*   For example: $235 = (2 \times 100) + (3 \times 10) + (5 \times 1)$

Computers use **Base 2 (Binary)**. It uses only two digits: `0` (Off) and `1` (On). The value is based on powers of 2.
*   For example, let's look at the binary number `1101`:

```
Bit position (from right):   3      2      1      0
Value of position:          2³     2²     2¹     2⁰
                            (8)    (4)    (2)    (1)
                          ┌──────┬──────┬──────┬──────┐
Binary Digits:            │  1   │  1   │  0   │  1   │
                          └──────┴──────┴──────┴──────┘
```
To convert `1101` to a normal number, just add the values where the bit is `1`:
$$\text{Value} = 8 + 4 + 0 + 1 = 13$$

---

### 4️⃣ How Negative Numbers are Stored (2's Complement)

How does a computer represent negative numbers like `-5` using only `0`s and `1`s?

The modern standard is called **2's Complement**. Here is the simple 3-step recipe to write a negative number:

1.  **Start with the positive number** (e.g., `5` in 8-bit binary):
    `00000101`
2.  **Flip all the bits** (change `0` to `1` and `1` to `0`):
    `11111010` (This is called 1's Complement)
3.  **Add 1** to the flipped bits:
    `11111011` (This is `-5`)

*Why do we do this?* Because this mathematical trick allows the computer to add and subtract numbers using the exact same hardware logic without needing a special sign handler.

---

### 5️⃣ Meet the Bitwise Operators

Think of bitwise operators as logic gates. Let's look at how they compare two bits:

#### 🤝 1. AND (`&`)
*   **Rule:** Output is `1` **only if** both inputs are `1`.
*   **Analogy:** You can only go on a trip if both parent A **and** parent B say "Yes".
*   **Example:** `5 & 3` (Binary: `0101 & 0011`)
    ```
      0 1 0 1  (5)
    & 0 0 1 1  (3)
    ─────────
      0 0 0 1  (Output is 1)
    ```

#### 👐 2. OR (`|`)
*   **Rule:** Output is `1` if **at least one** input is `1`.
*   **Analogy:** You can enter the room if you have ticket A **or** ticket B.
*   **Example:** `5 | 3` (Binary: `0101 | 0011`)
    ```
      0 1 0 1  (5)
    | 0 0 1 1  (3)
    ─────────
      0 1 1 1  (Output is 7)
    ```

#### 🔀 3. XOR (`^`)
*   **Rule:** Output is `1` if the inputs are **different**. Output is `0` if they are the same.
*   **Analogy:** A light switch. Flipping it changes the state. If two inputs are different, it outputs `1`.
*   **Example:** `5 ^ 3` (Binary: `0101 ^ 0011`)
    ```
      0 1 0 1  (5)
    ^ 0 0 1 1  (3)
    ─────────
      0 1 1 0  (Output is 6)
    ```

#### 🔄 4. NOT (`~`)
*   **Rule:** Flips every bit. `1` becomes `0`, and `0` becomes `1`.
*   **Formula:** `~x = -x - 1` (due to 2's complement).
*   **Example:** `~5` becomes `-6`.

#### 👈 5. Left Shift (`<<`)
*   **Rule:** Moves all bits to the left by $k$ places and fills empty spots on the right with `0`.
*   **Short Shortcut:** Shifting left by $k$ is the same as **multiplying by $2^k$**.
*   **Example:** `5 << 1` (Binary `0101` becomes `1010`, which is `10`).

#### 👉 6. Right Shift (`>>`)
*   **Rule:** Moves all bits to the right by $k$ places. Bits on the far right fall off.
*   **Short Shortcut:** Shifting right by $k$ is the same as **dividing by $2^k$** (ignoring remainders).
*   **Example:** `5 >> 1` (Binary `0101` becomes `0010`, which is `2`).

---

### 5️⃣ Basic Binary

| Decimal | Binary |
|---------|--------|
| 1       | 01     |
| 2       | 10     |
| 3       | 11     |
| 4       | 100    |
| 5       | 101    |
| 6       | 110    |
| 7       | 111    |
| 8       | 1000   |
| 9       | 1001   |
| 10      | 1010   |
| 11      | 1011   |
| 12      | 1100   |
| 13      | 1101   |
| 14      | 1110   |
| 15      | 1111   |
| 16      | 10000  |

### 6️⃣ Important Concept

#### 1. Even/Odd Check
```js
    n & 1
```
#### 2. Left Shift
```
    n << 1
```
Means: Multiply by 2

#### 3. Right Shift
```
    n >> 1
```
Means: Divide by 2

#### 4. Turn off last set bit
```
    n & (n-1)
```

Simple Declaration: It removes the last set bit (the rightmost `1`).

#### 5. Turn on last unset bit
```
    n | (n+1)
```
Simple Declaration: It turns the last unset bit (the rightmost `0`) to `1`.


### 5️⃣ The Python Traps (Very Important!)

If you use Python for interviews, you need to know about one major difference:

*   **Fixed-Width vs. Infinite Bits:**
    In languages like Java or C++, integers are restricted to exactly 32 bits. If a number grows past that, it overflows.
    In Python, integers have **infinite bits**. They can grow as large as your computer's memory allows.

*   **Why this is a trap:**
    If you flip bits of a number using `~` or perform shifts with negative numbers, Python doesn't cut them off at 32 bits. The bits keep going left forever.

*   **The Fix:**
    To make Python behave like a standard 32-bit machine, we use a mask: `0xFFFFFFFF` (which is binary for thirty-two `1`s).
    ```python
    # Force the result to stay within 32-bit unsigned boundaries:
    result = value & 0xFFFFFFFF
    ```

---

### 6️⃣ Common Interview Patterns

Most MAANG interview questions use one of these four ideas:

#### Pattern 1: The Magic XOR Cancelling Trick
Because $x \oplus x = 0$ (any number XORed with itself becomes 0) and $x \oplus 0 = x$:
*   If you have a list of numbers where every number appears twice except for one, XORing all the numbers together cancels out all the duplicates, leaving only the unique number!

#### Pattern 2: Power Set (Generating Subsets)
If you have a set of elements, say `[A, B, C]`, you can represent subsets using 3 bits:
*   `000` $\to$ No elements included: `[]`
*   `100` $\to$ Only A is included: `[A]`
*   `101` $\to$ A and C are included: `[A, C]`
By counting from $0$ to $7$ ($2^3 - 1$), you can easily generate all subsets!

#### Pattern 3: Clearing the lowest set bit (Brian Kernighan's Algorithm)
If you want to count how many `1`s are in a binary number:
*   Instead of checking every single bit one by one, use `n = n & (n - 1)`.
*   Each time you do this, the lowest `1` in the number disappears.
*   Count how many times you can do this before the number becomes `0`. This is the exact number of `1`s.

---

### 7️⃣ Solved Beginner Problems

Here are the basic code templates for the interview favorites:

#### 💡 Problem 1: Find the Single Number (LeetCode 136)
> Find the element in a list that appears only once, while all others appear twice.

```python
def single_number(nums):
    result = 0
    for num in nums:
        result ^= num  # Duplicates cancel out
    return result
```

#### 💡 Problem 2: Count the 1 Bits (LeetCode 191)
> Count how many `1`s are in the binary representation of a number.

```python
def hamming_weight(n):
    count = 0
    while n != 0:
        n = n & (n - 1)  # Removes the rightmost 1 bit
        count += 1
    return count
```

#### 💡 Problem 3: Generate All Subsets (LeetCode 78)
> Given a list of numbers, return all possible combinations (subsets).

```python
def subsets(nums):
    n = len(nums)
    total_subsets = 1 << n  # This is 2^n
    result = []
    
    for mask in range(total_subsets):
        current_subset = []
        for j in range(n):
            # If the j-th bit of the mask is 1, include nums[j]
            if (mask & (1 << j)) != 0:
                current_subset.append(nums[j])
        result.append(current_subset)
        
    return result
```

#### 💡 Problem 4: Sum of Two Integers without + or - (LeetCode 371)
> Add two numbers without using `+` or `-`.

```python
def get_sum(a, b):
    mask = 0xFFFFFFFF  # Mask to simulate 32-bit integer
    
    while b != 0:
        temp_sum = (a ^ b) & mask         # XOR sums bits without carry
        carry = ((a & b) << 1) & mask      # AND finds carries, shifted left
        a = temp_sum
        b = carry
        
    # If a is a negative number in 32-bit signed format
    if a >= 0x80000000:
        return a - 0x100000000
    return a
```

---

### 8️⃣ Practice Path (Where to Start)

Go to LeetCode and solve these problems in this order:

1.  [136. Single Number](https://leetcode.com/problems/single-number/) (Easy) — *Practices XOR properties.*
2.  [191. Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/) (Easy) — *Practices bit counting.*
3.  [231. Power of Two](https://leetcode.com/problems/power-of-two/) (Easy) — *Practices check logic.*
4.  [268. Missing Number](https://leetcode.com/problems/missing-number/) (Easy) — *Another great XOR practice.*
5.  [78. Subsets](https://leetcode.com/problems/subsets/) (Medium) — *Practices state representation and masking.*