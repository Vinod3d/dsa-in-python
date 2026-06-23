# 🔄Recursion

Recursion is one of the most powerful concept in programming, yet it is often the biggest hurdle for DSA beginners. If you want to crack interviews at **Google, Meta, Netflix, Amazon, or Microsoft**, you **must** master recursion, because it forms the foundation for:
- 🌳 Trees & Graphs (DFS, Traversals)
- ↩️ Backtracking (N-Queens, Sudoku Solver)
- 📈 Dynamic Programming (Memoization, Tabulation)
- 🔀 Divide and Conquer (Merge Sort, Quick Sort)

This guide is designed for absolute beginners to build a strong foundation and transition into interview-ready recursion thinking.


## 1️⃣ What is Recursion?

 **Recursion is a process where a function calls itself to solve a smaller version of the same problem.**

### 🧸 Real-World Analogy: Russian Nesting Dolls (Matryoshka Dolls)
Imagine you have a large nesting doll. 
1. You open the outer doll (the main problem).
2. Inside, you find another slightly smaller doll (a sub-problem).
3. You keep opening them one by one (calling the function with smaller inputs).
4. Eventually, you reach the smallest doll which **cannot be opened anymore**. This is where you stop. In programming, we call this the **Base Case**.
5. Once you reach the smallest doll, you can start closing/assembling them back up (returning values up the chain).

```
[ Big Doll ] ──> calls ──> [ Medium Doll ] ──> calls ──> [ Smallest Doll ] (Base Case: Stop!)
     │                                                           │
     └────── returns value ◄────── returns value ◄───────────────┘
```

---

## 2️⃣ The Core Components of a Recursive Function

Every recursive function must have two main ingredients:

1. **The Base Case (The Stop Button):** The condition where the function stops calling itself. Without a basecase, your program will run forever and crash.
2. **The Recursive Work / Relation:** The step where the function calls itself with a **smaller/different input** to do the work.

### 🚫 The Danger: Stack Overflow
If you forget the **Base Case**, or if your input doesn't get smaller, the function will call itself infinitely. 
Since every function call consumes memory on the **Call Stack**, an infinite loop will eventually consume all available memory, causing a crash known as **Stack Overflow**.

---

## 3️⃣ Visualizing the Call Stack (Under the Hood)

Let's see what happens in the computer's memory (RAM) when a recursive function runs. 

We will write a function to calculate the **Factorial of a number ($N!$)**. 
> **Mathematical definition of Factorial:**
> $5! = 5 \times 4 \times 3 \times 2 \times 1 = 120$
> $N! = N \times (N - 1)!$
> Base Case: $0! = 1$ or $1! = 1$

Here is the Python code:

```python
def factorial(n):
    # 1. Base Case
    if n == 1:
        return 1
    
    # 2. Recursive Relation / Work
    return n * factorial(n - 1)
```

### 🧠 The Call Stack Simulation for `factorial(3)`

The Call Stack works like a stack of plates. You add plates on top (**Push**) and remove plates from the top (**Pop**).

#### Phase 1: Going Down the Stack (Winding Phase)
1. `factorial(3)` is called. It needs `factorial(2)` to compute its result. It pauses and waits.
2. `factorial(2)` is called. It needs `factorial(1)` to compute its result. It pauses and waits.
3. `factorial(1)` is called. This hits the **Base Case** and returns `1` immediately.

```
|                  |
|  factorial(1)    | --> Hits Base Case! Returns 1.
|__________________|
|  factorial(2)    | --> Waiting for factorial(1)...
|__________________|
|  factorial(3)    | --> Waiting for factorial(2)...
|__________________|
   CALL STACK
```

#### Phase 2: Coming Up the Stack (Unwinding Phase)
Now, the results bubble back up:
1. `factorial(1)` returns `1` and is popped off the stack.
2. `factorial(2)` resumes: `2 * factorial(1)` becomes `2 * 1 = 2`. It returns `2` and is popped.
3. `factorial(3)` resumes: `3 * factorial(2)` becomes `3 * 2 = 6`. It returns `6` (Final Answer!).

```
Step 1: factorial(1) returns 1
Step 2: factorial(2) returns 2 * 1 = 2
Step 3: factorial(3) returns 3 * 2 = 6
```

---

## 4️⃣ The 3-Step Formula to Solve Any Recursion Problem

When you see a recursion problem in an interview, do not start coding immediately. Follow this formula:

### 🛠️ Step 1: Identify the Base Case
Ask yourself: *“What is the simplest possible input for this problem where the answer is obvious and I can return it immediately?”*
* e.g., For sum of numbers, it's $N = 0$. For string reversal, it's an empty string `""`.

### 🛠️ Step 2: Find the Sub-Problem (Recursive Relation)
Ask yourself: *“How can I express this problem in terms of a smaller version of itself?”*
* e.g., $Sum(N) = N + Sum(N - 1)$.

### 🛠️ Step 3: Do the Dry Run (Draw the Recursion Tree)
Trace the calls manually for a small input (like $N=3$) using a diagram. This helps verify that your base case is reachable and logic is correct.

---

## 5️⃣ Common Types of Recursion

Understanding these types will help you design efficient recursive algorithms.

### A. Tail Recursion vs. Non-Tail Recursion
* **Tail Recursion:** The recursive call is the **very last statement** executed by the function. No operations are done after the recursive call. Modern compilers can optimize tail-recursive functions to use $O(1)$ stack space (Tail Call Optimization - TCO).
  ```python
  # Tail Recursive (No work left after the call)
  def print_n_to_1(n):
      if n == 0:
          return
      print(n)
      print_n_to_1(n - 1)
  ```
* **Non-Tail Recursion:** The function performs some calculations *after* the recursive call returns.
  ```python
  # Non-Tail Recursive (We must multiply by n after factorial(n-1) returns)
  def factorial(n):
      if n == 1:
          return 1
      return n * factorial(n - 1)
  ```

### B. Linear Recursion vs. Tree Recursion
* **Linear Recursion:** The function makes **only one** recursive call per execution.
  * *Example:* Factorial, Sum of N numbers, Binary Search.
* **Tree Recursion:** The function makes **two or more** recursive calls per execution. This forms a tree-like structure of calls.
  * *Example:* Fibonacci numbers ($Fib(n) = Fib(n-1) + Fib(n-2)$), Merge Sort.

---

## 6️⃣ Must-Solve Recursion Problems (With Dry Runs)

Let's look at 5 essential beginner-to-intermediate problems that are frequently asked in MAANG phone screening and coding rounds.

---

### 📌 Problem 1: Print 1 to N (Understanding Head vs. Tail)

Write a recursive function to print numbers from 1 to $N$.

#### 💡 Strategy:
If we want to print from 1 to $N$, we can:
1. Make a recursive call first to print numbers from $1$ to $N-1$.
2. Print $N$ after the recursive call returns. (This is called **Head Recursion** logic).

#### Python Code:
```python
def print_1_to_n(n):
    # Base Case
    if n == 0:
        return
    
    # Recursive Call (Ask recursion to print 1 to n-1 first)
    print_1_to_n(n - 1)
    
    # Self Work (Print the current number)
    print(n, end=" ")

# Example Run
print_1_to_n(5)
# Output: 1 2 3 4 5
```

#### 🌳 Dry Run Tree for `print_1_to_n(3)`:
```
print_1_to_n(3)
  ├── calls print_1_to_n(2)
  │     ├── calls print_1_to_n(1)
  │     │     ├── calls print_1_to_n(0) --> Hits Base Case, returns nothing.
  │     │     └── prints 1
  │     └── prints 2
  └── prints 3
```

* **Time Complexity:** $O(N)$ because we make $N$ function calls.
* **Space Complexity:** $O(N)$ auxiliary stack space.

---

### 📌 Problem 2: Sum of Digits of a Number

Given an integer $N$ (e.g., $1234$), find the sum of all its digits ($1 + 2 + 3 + 4 = 10$).

#### 💡 Strategy:
- **Base Case:** If the number is $0$, the sum of its digits is $0$.
- **Recursive Relation:** Extract the last digit using `% 10` and add it to the sum of the remaining digits (`n // 10`).
- Formula: $SumOfDigits(N) = (N \% 10) + SumOfDigits(N // 10)$

#### Python Code:
```python
def sum_of_digits(n):
    # Base Case
    if n == 0:
        return 0
    
    # Recursive Work
    last_digit = n % 10
    remaining_number = n // 10
    
    return last_digit + sum_of_digits(remaining_number)

# Example Run
print(sum_of_digits(1234))  # Output: 10
```

#### 🌳 Dry Run for `sum_of_digits(123)`:
```
sum_of_digits(123)
  = 3 + sum_of_digits(12)
          = 2 + sum_of_digits(1)
                  = 1 + sum_of_digits(0)
                          = 0 (Base case)
                  = 1 + 0 = 1
          = 2 + 1 = 3
  = 3 + 3 = 6 (Final Answer)
```

* **Time Complexity:** $O(\log_{10} N)$ – The number of digits in $N$.
* **Space Complexity:** $O(\log_{10} N)$ – Stack space proportional to the number of digits.

---

### 📌 Problem 3: N-th Fibonacci Number (Tree Recursion)

The Fibonacci sequence is: `0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...`
Find the $N$-th Fibonacci number. ($Fib(0) = 0$, $Fib(1) = 1$, $Fib(2) = 1$, $Fib(3) = 2$, etc.)

#### 💡 Strategy:
- **Base Case:** If $N == 0$, return $0$. If $N == 1$, return $1$.
- **Recursive Relation:** $Fib(N) = Fib(N - 1) + Fib(N - 2)$

#### Python Code:
```python
def fib(n):
    # Base Cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Tree Recursion: Two calls per function
    return fib(n - 1) + fib(n - 2)

# Example Run
print(fib(4))  # Output: 3
```

#### 🌳 Dry Run Tree for `fib(4)`:
```
                    fib(4)
                   /      \
               fib(3)      fib(2)
              /      \     /     \
          fib(2)   fib(1) fib(1) fib(0)
          /    \     (1)    (1)   (0)
      fib(1)  fib(0)
       (1)     (0)
```
*Notice how some calls like `fib(2)` are solved multiple times. This is why basic tree recursion is slow and leads to Memoization in Dynamic Programming.*

* **Time Complexity:** $O(2^N)$ – Exponential! The number of calls doubles at each level.
* **Space Complexity:** $O(N)$ – The maximum depth of the call stack is equal to the height of the tree, which is $N$.

---

### 📌 Problem 4: Binary Search using Recursion

Search for a target value in a sorted array using recursion.

#### 💡 Strategy:
- **Base Case:** If `left > right`, the element is not present. Return `-1`.
- **Recursive Relation:** Find the middle element (`mid`).
  - If `arr[mid] == target`, return `mid`.
  - If `arr[mid] > target`, search the left half: call `binary_search(arr, left, mid - 1, target)`.
  - If `arr[mid] < target`, search the right half: call `binary_search(arr, mid + 1, right, target)`.

#### Python Code:
```python
def binary_search_recursive(arr, left, right, target):
    # Base Case: Range is invalid (element not found)
    if left > right:
        return -1
    
    mid = left + (right - left) // 2
    
    # Base Case: Found the target
    if arr[mid] == target:
        return mid
    
    # Recursive Case 1: Target is smaller, look left
    if arr[mid] > target:
        return binary_search_recursive(arr, left, mid - 1, target)
    
    # Recursive Case 2: Target is larger, look right
    return binary_search_recursive(arr, mid + 1, right, target)

# Example Run
arr = [1, 3, 5, 7, 9, 11]
print(binary_search_recursive(arr, 0, len(arr) - 1, 7))  # Output: 3
```

* **Time Complexity:** $O(\log N)$ – We split the search space in half at each step.
* **Space Complexity:** $O(\log N)$ – Stack space used by recursive frames.

---

### 📌 Problem 5: Generate all Subsequences of a String (Power Set)
*🔥 Highly Asked in MAANG interviews (Amazon, Google, Meta)*

Given a string (e.g., `"abc"`), print all its subsequences. A subsequence is a sequence of characters that can be derived by deleting some or no characters without changing the order of the remaining characters.
For `"abc"`, the subsequences are: `""`, `"a"`, `"b"`, `"c"`, `"ab"`, `"ac"`, `"bc"`, `"abc"`.

#### 💡 Strategy: The "Include / Exclude" Pattern
For every character in the string, we have two choices:
1. **Include** the character in our current subset.
2. **Exclude** the character from our current subset.

#### Python Code:
```python
def find_subsequences(s, index, current_subset):
    # Base Case: If we have processed all characters
    if index == len(s):
        print(f'"{current_subset}"')
        return
    
    # Choice 1: Include the current character s[index]
    find_subsequences(s, index + 1, current_subset + s[index])
    
    # Choice 2: Exclude the current character s[index]
    find_subsequences(s, index + 1, current_subset)

# Example Run
find_subsequences("abc", 0, "")
```

#### 🌳 Recursion Tree for `find_subsequences("abc")`:
```
                             index=0 ("")
                            /            \ (Exclude s[0])
                    index=1 ("a")       index=1 ("")
                    /           \        /          \
              index=2 ("ab")  index=2("a")  ("b")    ("")
              /       \       /     \      /    \    /   \
           ("abc")  ("ab") ("ac")  ("a") ("bc")("b")("c") ("")
```

* **Time Complexity:** $O(2^N)$ – Since there are $2$ options for each of the $N$ characters, we have $2^N$ leaf nodes.
* **Space Complexity:** $O(N)$ – The maximum depth of the call stack is $N$ (the length of the string).

---

## 7️⃣ MAANG Secrets: Tips to Analyze Time & Space Complexity

During MAANG interviews, you must always state the Time and Space Complexity of your solution. Here is how you do it for recursion:

### ⏱️ Time Complexity Analysis
To find the time complexity, calculate:
$$\text{Total Time Complexity} = (\text{Total Number of Recursive Calls}) \times (\text{Time spent inside one function call})$$

* **Linear Recursion (e.g., Factorial):** We make $N$ calls, and inside each call, we do $O(1)$ work (multiplication).
  $$\text{Time} = N \times O(1) = O(N)$$
* **Tree Recursion (e.g., Fibonacci):** The tree height is $N$, and at each step, the calls branch into 2. The total nodes in a perfect binary tree of height $N$ is $2^N$.
  $$\text{Time} = O(2^N)$$

### 💾 Space Complexity Analysis
For iterative code, space complexity is just the extra variables or arrays you create. 
**For recursion, space complexity ALWAYS includes the Auxiliary Stack Space.** This is the maximum depth of the call stack at any point in time.

$$\text{Stack Space Complexity} = \text{Maximum depth of the recursion tree}$$

* For `fib(n)`, even though there are $2^N$ total calls, the maximum height of the stack at any single moment is $O(N)$ because once a branch finishes executing, its frames are popped off the stack. Hence, Stack Space is $O(N)$.

---

## 8️⃣ Next Steps: Your Path to Mastery
1. **Dry run every problem on paper.** Do not just write code. Draw the stack frames and the tree.
2. Practice these LeetCode problems:
   - [ ] [LeetCode 509: Fibonacci Number (Easy)](https://leetcode.com/problems/fibonacci-number/)
   - [ ] [LeetCode 344: Reverse String (Easy)](https://leetcode.com/problems/reverse-string/)
   - [ ] [LeetCode 206: Reverse Linked List (Easy/Medium)](https://leetcode.com/problems/reverse-linked-list/)
   - [ ] [LeetCode 78: Subsets (Medium)](https://leetcode.com/problems/subsets/)
   - [ ] [LeetCode 17: Letter Combinations of a Phone Number (Medium)](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)
3. Move on to **07_Sorting** (where we use Merge Sort and Quick Sort recursion) or **18_Backtracking** to see recursion's real power!
