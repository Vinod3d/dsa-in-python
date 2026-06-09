# Hashing in Data Structures and Algorithms (DSA)

## Index

| No. | Topic                                                                                        |
| --- | -------------------------------------------------------------------------------------------- |
| 1   | [Introduction to Hashing](#1-introduction-to-hashing)                                        |
| 2   | [What is a Hash Function?](#2-what-is-a-hash-function)                                       |
| 3   | [Characteristics of a Good Hash Function](#3-characteristics-of-a-good-hash-function)        |
| 4   | [Hash Table](#4-hash-table)                                                                  |
| 5   | [Working of Hashing](#5-working-of-hashing)                                                  |
| 6   | [Collision in Hashing](#6-collision-in-hashing)                                              |
| 7   | [Collision Resolution Techniques](#7-collision-resolution-techniques)                        |
| 8   | [Separate Chaining](#8-separate-chaining)                                                    |
| 9   | [Open Addressing](#9-open-addressing)                                                        |
| 10  | [Linear Probing](#10-linear-probing)                                                         |
| 11  | [Quadratic Probing](#11-quadratic-probing)                                                   |
| 12  | [Double Hashing](#12-double-hashing)                                                         |
| 13  | [Load Factor](#13-load-factor)                                                               |
| 14  | [Rehashing](#14-rehashing)                                                                   |
| 15  | [Time Complexity of Hashing](#15-time-complexity-of-hashing)                                 |
| 16  | [Applications of Hashing](#16-applications-of-hashing)                                       |
| 17  | [Advantages of Hashing](#17-advantages-of-hashing)                                           |
| 18  | [Disadvantages of Hashing](#18-disadvantages-of-hashing)                                     |
| 19  | [Hashing in Different Programming Languages](#19-hashing-in-different-programming-languages) |
| 20  | [Important Interview Questions](#20-important-interview-questions)                           |

---

# 1. Introduction to Hashing

Hashing is a technique used to store and retrieve data quickly.
It converts a large amount of data into a small fixed-size value called a **hash value** or **hash code**.

Hashing is mainly used for:

* Fast searching
* Fast insertion
* Fast deletion

Instead of searching data one by one, hashing directly calculates the memory location where data should be stored.

Hashing is one of the most important concepts in DSA because many real-world systems use it internally.

Examples:

* Password storage
* Database indexing
* Caching systems
* Dictionaries
* Maps
* Sets

---

# 2. What is a Hash Function?

A **Hash Function** is a mathematical function that converts a key into an index value.

The generated index determines where the element will be stored in the hash table.

## General Formula

h(k)=k\bmod m

Where:

* `h(k)` = hash value
* `k` = key
* `m` = size of hash table

---

## Example

Suppose table size = 10

Key = 25

Then:

h(25)=25\bmod10=5

So, key 25 will be stored at index 5.

---

# 3. Characteristics of a Good Hash Function

A good hash function should have the following properties:

## 1. Fast Computation

The hash value should be calculated quickly.

## 2. Uniform Distribution

Data should be distributed evenly across the table.

## 3. Minimum Collisions

Different keys should produce different hash values whenever possible.

## 4. Deterministic

The same key should always generate the same hash value.

Example:

If key 50 gives index 2 today, it should always give index 2.

---

# 4. Hash Table

A **Hash Table** is a data structure that stores data using hashing.

It consists of:

* Keys
* Values
* Hash function
* Array structure

---

## Structure of Hash Table

| Index | Data  |
| ----- | ----- |
| 0     | Empty |
| 1     | 21    |
| 2     | 32    |
| 3     | Empty |
| 4     | 14    |

---

# 5. Working of Hashing

The process of hashing works in the following steps:

## Step 1: Take Input Key

Example:

```text
Key = 45
```

## Step 2: Apply Hash Function

```text
h(45) = 45 % 10 = 5
```

## Step 3: Store Data

Store the element at index 5.

---

# 6. Collision in Hashing

A collision occurs when two different keys generate the same hash value.

---

## Example

Suppose table size = 10

```text
h(25) = 25 % 10 = 5
h(35) = 35 % 10 = 5
```

Both keys want to store at index 5.

This situation is called **Collision**.

---

# 7. Collision Resolution Techniques

The following techniques are used to handle collisions:

| Technique         | Description               |
| ----------------- | ------------------------- |
| Separate Chaining | Uses linked list          |
| Linear Probing    | Searches sequentially     |
| Quadratic Probing | Uses quadratic jumps      |
| Double Hashing    | Uses second hash function |

---

# 8. Separate Chaining

In Separate Chaining, each index contains a linked list.

If multiple elements hash to the same index, they are stored in the linked list.

---

## Example

```text
Index 5 → 25 → 35 → 45
```

---

## Advantages

* Easy to implement
* Handles many collisions

## Disadvantages

* Extra memory required
* Linked list traversal needed

---

# 9. Open Addressing

In Open Addressing, all elements are stored inside the table itself.

If collision occurs, another empty position is searched.

Types:

* Linear Probing
* Quadratic Probing
* Double Hashing

---

# 10. Linear Probing

In Linear Probing, if a collision occurs, search sequentially for the next empty slot.

---

## Formula

(h(k)+i)\bmod m

Where:

* `i` = probe number

---

## Example

Suppose:

```text
Table size = 10
Keys = 25, 35
```

```text
25 % 10 = 5
35 % 10 = 5
```

25 is stored at index 5.

35 collides, so check:

```text
Index 6
```

If empty, store there.

---

## Problem: Clustering

Many consecutive filled positions create clusters.

This decreases performance.

---

# 11. Quadratic Probing

Quadratic probing uses square values to find the next position.

---

## Formula

(h(k)+i^2)\bmod m

---

## Example

If collision occurs at index 5:

Check:

```text
5 + 1² = 6
5 + 2² = 9
5 + 3² = 14
```

---

## Advantages

* Reduces clustering

## Disadvantages

* More complex than linear probing

---

# 12. Double Hashing

Double hashing uses another hash function.

---

## Formula

(h_1(k)+i\times h_2(k))\bmod m

---

## Advantages

* Better distribution
* Less clustering

## Disadvantages

* Complex implementation

---

# 13. Load Factor

Load factor indicates how full the hash table is.

---

## Formula

\lambda=\frac{n}{m}

Where:

* `n` = number of elements
* `m` = size of table

---

## Example

If:

```text
Elements = 7
Table size = 10
```

Then:

```text
Load Factor = 7 / 10 = 0.7
```

---

# 14. Rehashing

Rehashing means increasing the size of the hash table and reinserting elements.

It is done when load factor becomes high.

---

## Why Rehashing?

High load factor causes:

* More collisions
* Slower searching
* Reduced performance

---

## Steps of Rehashing

1. Create larger table
2. Recalculate hash values
3. Insert all elements again

---

# 15. Time Complexity of Hashing

| Operation | Average Case | Worst Case |
| --------- | ------------ | ---------- |
| Search    | O(1)         | O(n)       |
| Insert    | O(1)         | O(n)       |
| Delete    | O(1)         | O(n)       |

---

# 16. Applications of Hashing

Hashing is widely used in computer science.

---

## 1. Password Storage

Passwords are stored as hash values for security.

---

## 2. Databases

Databases use hashing for indexing and fast search.

---

## 3. Caches

Web browsers and servers use hashing for caching.

---

## 4. Dictionaries and Maps

Programming languages use hashing internally.

Examples:

* HashMap in Java
* Dictionary in Python
* unordered_map in C++

---

## 5. Blockchain

Cryptographic hashing is used in blockchain technology.

---

# 17. Advantages of Hashing

## 1. Very Fast Operations

Searching, insertion, and deletion are very fast.

## 2. Efficient Data Retrieval

Data can be accessed directly.

## 3. Widely Used

Used in many real-world applications.

---

# 18. Disadvantages of Hashing

## 1. Collision Problem

Different keys may map to the same location.

## 2. Memory Wastage

Unused spaces may remain empty.

## 3. No Ordering

Data is not stored in sorted order.

---

# 19. Hashing in Different Programming Languages

## Java

```java
HashMap<Integer, String> map = new HashMap<>();
```

---

## Python

```python
data = {
    1: "Apple",
    2: "Banana"
}
```

---

## C++

```cpp
unordered_map<int, string> mp;
```

---

# 20. Important Interview Questions

## Basic Questions

1. What is hashing?
2. What is a hash function?
3. What is collision?
4. What is load factor?
5. Difference between hashing and indexing?

---

## Intermediate Questions

1. Explain collision resolution techniques.
2. Difference between chaining and open addressing.
3. What is clustering?
4. Explain rehashing.
5. Why is hashing faster?

---

## Advanced Questions

1. Design a custom hash table.
2. Explain cryptographic hashing.
3. Compare HashMap and TreeMap.
4. What happens internally in HashMap?
5. How does hashing work in distributed systems?

---

# Summary

Hashing is a powerful technique used for fast data storage and retrieval.

Main concepts include:

* Hash Function
* Hash Table
* Collision
* Chaining
* Probing
* Load Factor
* Rehashing

Hashing provides near constant-time complexity for most operations, making it one of the most important topics in DSA and system design.
