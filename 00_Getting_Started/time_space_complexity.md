

# Time and Space Complexity ⏱️📦

Understanding **Time and Space Complexity** is crucial in DSA because it tells us  
**how efficient an algorithm is** and **how well it scales** with large inputs.

In interviews, **good logic + bad complexity = rejection**.

---

## 📌 What is Time Complexity?

**Time Complexity** measures:
> How much time an algorithm takes to run as input size increases.

It does NOT calculate exact seconds.  
It measures **growth rate**.

📌 Focus is on:
- Number of operations
- Relation with input size (n)

---

## 📌 What is Space Complexity?

**Space Complexity** measures:
> How much extra memory an algorithm uses.

Includes:
- Variables
- Data structures
- Recursive call stack

👉 Input memory is usually not counted.

---

## 🧠 Why Time & Space Complexity Matters

- Computers have limited resources
- Large inputs can crash slow algorithms
- Interviewers want **optimized thinkers**
- FAANG systems deal with **millions of users**

Example:
- `n = 10⁵`
- O(n²) → ❌ too slow
- O(n log n) → ✅ acceptable

---

## 📊 Big-O Notation (MOST IMPORTANT)

Big-O describes **worst-case performance**.

| Notation | Meaning | Example |
|--------|--------|--------|
| O(1) | Constant | Access array element |
| O(log n) | Logarithmic | Binary Search |
| O(n) | Linear | Loop through array |
| O(n log n) | Linearithmic | Merge Sort |
| O(n²) | Quadratic | Nested loops |
| O(2ⁿ) | Exponential | Subsets |
| O(n!) | Factorial | Permutations |

---

## 🚦 Order of Growth (Fast → Slow)

```

O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ) < O(n!)

````

👉 Interviewers expect you to know this order.

---

## 📌 Best, Average & Worst Case

| Case | Meaning |
|----|-------|
| Best | Minimum time |
| Average | Expected time |
| Worst | Maximum time |

📌 Example: Linear Search
- Best: element at start → O(1)
- Worst: element at end → O(n)

👉 Big-O usually considers **worst case**.

---

## 🧮 How to Calculate Time Complexity

### 1️⃣ Single Loop
```python
for i in range(n):
    print(i)
````

⏱️ Time: **O(n)**

---

### 2️⃣ Nested Loop

```python
for i in range(n):
    for j in range(n):
        print(i, j)
```

⏱️ Time: **O(n²)**

---

### 3️⃣ Loop with Halving

```python
while n > 0:
    n //= 2
```

⏱️ Time: **O(log n)**

---

### 4️⃣ Multiple Loops (Sequential)

```python
for i in range(n):
    pass
for j in range(n):
    pass
```

⏱️ Time: **O(n)**
(Not O(2n), constants ignored)

---

## ✂️ Ignoring Constants & Lower Terms

Big-O ignores:

* Constants
* Smaller terms

Examples:

* O(3n) → O(n)
* O(n² + n) → O(n²)

👉 Focus on dominant term.

---

## 📦 Space Complexity Examples

### Constant Space

```python
sum = 0
```

📦 Space: **O(1)**

---

### Extra Array

```python
arr = [0] * n
```

📦 Space: **O(n)**

---

### Recursive Call Stack

```python
def func(n):
    if n == 0:
        return
    func(n-1)
```

📦 Space: **O(n)** (call stack)

---

## 🔥 Why O(n²) is Bad

For `n = 10⁵`:

* O(n²) → 10¹⁰ operations ❌
* Program will timeout or crash

📌 Interviewers often ask:

> “Can you optimize this?”

---

## ⚡ Time–Space Tradeoff

Sometimes:

* Use extra memory to save time

Example:

* Without hashing → O(n²)
* With hashmap → O(n) time + O(n) space

👉 This tradeoff is **interview favorite**.

---

## 🧠 Complexity of Common DSA Operations

| Operation             | Complexity |
| --------------------- | ---------- |
| Array access          | O(1)       |
| Array search          | O(n)       |
| HashMap lookup        | O(1)       |
| Stack push/pop        | O(1)       |
| Queue enqueue/dequeue | O(1)       |
| Tree traversal        | O(n)       |
| Graph traversal       | O(V + E)   |

---

## 🎯 How Interviewers Expect You to Answer

When asked complexity:
Say clearly:

```
Time Complexity: O(n)
Space Complexity: O(1)
```

Then explain **why**.

❌ Wrong:

> “I think it will be fast”

✅ Correct:

> “We traverse array once, so O(n)”

---

## ❌ Common Mistakes

* Forgetting space complexity
* Saying wrong Big-O
* Ignoring recursion stack
* Confusing O(log n) and O(n)

---

## ✅ Interview Tips (VERY IMPORTANT)

* Always mention complexity
* Optimize if asked
* Never guess
* Be confident and clear
* Practice analyzing code daily

---

## 🧠 Golden Rule

> **First write correct code, then optimize it**

Correct + optimized = selection.

---

## 🎯 Final Summary

* Time complexity = performance
* Space complexity = memory usage
* Big-O = growth rate
* Interviewers care about **efficiency thinking**

If you master this topic:

* 50% DSA interview fear is gone
