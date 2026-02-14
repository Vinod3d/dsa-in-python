## DSA in **Array** and **List** in Python

In Data Structures and Algorithms (DSA), **Array** is one of the most basic and important data structures.
In Python, we mainly use **List** as an implementation of an array.

---

# 1️⃣ What is an Array?

An **array** is a collection of elements stored in **contiguous memory locations**.
All elements usually have the **same data type**.

### Example (Concept):

```
Index:   0   1   2   3
Array:  [10, 20, 30, 40]
```

Each element can be accessed using its **index**.

---

# 2️⃣ Array in Python

Python does not have a traditional built-in array like C/C++.
Instead, we use:

* **List** (most common)
* NumPy array (for numerical work)
* array module (`import array`)

For DSA practice, we mostly use **List**.

---

# 3️⃣ What is a List in Python?

A **list** is a dynamic array in Python.

### Example:

```python
arr = [10, 20, 30, 40]
```

✔ Ordered
✔ Mutable (can change values)
✔ Can store different data types

---

# 4️⃣ Basic Operations in Array/List (Important for DSA)

## 1. Access Element – O(1)

```python
arr[2]   # 30
```

## 2. Insert Element

### (a) At End – O(1)

```python
arr.append(50)
```

### (b) At Beginning – O(n)

```python
arr.insert(0, 5)
```

## 3. Delete Element

### (a) Remove by value – O(n)

```python
arr.remove(20)
```

### (b) Remove by index – O(n)

```python
arr.pop(1)
```

## 4. Traversal – O(n)

```python
for num in arr:
    print(num)
```

## 5. Searching

### (a) Linear Search – O(n)

```python
if 30 in arr:
    print("Found")
```

### (b) Binary Search – O(log n)

(Only works on sorted array)

Python provides binary search in:

* Python Software Foundation standard library (`bisect` module)

---

# 5️⃣ Time Complexity Summary

| Operation       | Time Complexity |
| --------------- | --------------- |
| Access          | O(1)            |
| Append          | O(1)            |
| Insert (middle) | O(n)            |
| Delete          | O(n)            |
| Search          | O(n)            |

---

# 6️⃣ Why Array/List is Important in DSA?

Almost every DSA problem starts with arrays:

* Sorting
* Searching
* Sliding Window
* Two Pointer
* Prefix Sum
* Kadane’s Algorithm
* Subarrays problems

If you master arrays, 40–50% beginner DSA problems become easy.

---

# 7️⃣ Example DSA Problem

### Find Maximum Element in Array

```python
arr = [5, 2, 9, 1, 7]

maximum = arr[0]

for num in arr:
    if num > maximum:
        maximum = num

print(maximum)
```

**Time Complexity:** O(n)
**Space Complexity:** O(1)
