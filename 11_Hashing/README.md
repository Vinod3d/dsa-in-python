## 1️⃣ Why Do We Need Hashing?

Imagine you have:

* 1 million student records
* You want to search student with roll number **105432**

If you store them in a normal list:

* You may need to check one by one
* That takes **O(n)** time (slow)

But with hashing:

* You can directly jump to the correct location
* That takes **O(1)** time (very fast)

👉 That is why hashing is powerful.

---

## 2️⃣ What is Hashing?

Hashing is a powerful technique used in data structures to store and retrieve data efficiently. It works by transforming a given input value (called a key) into a small numerical value using a special function known as a hash function.

This numerical value is called an index, and it represents the position where the data will be stored inside a structure called a hash table (which is basically an array).

Instead of searching through all elements one by one, hashing allows us to directly jump to the exact position where the data should be stored or found. This is what makes hashing extremely fast.

```
Key → Hash Function → Index → Store Data
```

---

## 3️⃣ What is a Hash Function?

A hash function is just a formula that converts large data into a small number (index).

Example:

```
H(x) = x % 10
```

If:

```
x = 123
123 % 10 = 3
```

So index = 3

This means the data will be stored at position 3 in the array.

---

## 4️⃣ What is a Hash Table?

A hash table is simply an array.

Example:

```
Index:  0 1 2 3 4 5 6 7 8 9
Value:  _ _ _ _ _ _ _ _ _ _
```

If we insert 25:

```
H(25) = 25 % 10 = 5
```

Store at index 5.

If we insert 42:

```
42 % 10 = 2
```

Store at index 2.

Now searching becomes very fast:

To search 25 → directly go to index 5.

No need to check every element.

---

## 5️⃣ Why is Hashing O(1)?

Because:

* We are not searching the whole array
* We directly calculate the index
* Then access that location

So:

| Operation | Time (Average) |
| --------- | -------------- |
| Insert    | O(1)           |
| Search    | O(1)           |
| Delete    | O(1)           |

---

## 6️⃣ What is Collision?

Sometimes two keys give the same index.

Example:

```
25 % 10 = 5
35 % 10 = 5
```

Both want index 5.

This is called **collision**.

Collision is normal in hashing.

---

## 7️⃣ How Do We Handle Collision?

There are two common methods:

### ✅ 1. Chaining

Store multiple elements in the same index using a list.

Example:

```
Index 5 → [25, 35]
```

### ✅ 2. Open Addressing

If one index is full, find the next empty position.

* Linear probing
* Quadratic probing
* Double hashing

Python handles this internally.

---

## 8️⃣ Hashing in Python

In Python:

* `dict` uses hashing
* `set` uses hashing

### Example:

```python
data = {}

data["apple"] = 10
data["banana"] = 20

print(data["apple"])
```

Python automatically:

* Hashes the key
* Stores it
* Retrieves in O(1)

---

## 9️⃣ Where is Hashing Used in DSA?

Hashing is extremely important for:

* Frequency counting
* Two Sum problem
* Finding duplicates
* Checking anagrams
* Subarray sum problems
* Caching
* Databases

---

## 🔟 When Does Hashing Become Slow?

Worst case:

If too many collisions happen
Then time complexity becomes:

```
O(n)
```

But good hash functions reduce collisions.
