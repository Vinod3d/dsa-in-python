# 03. Arrays & Dynamic Lists in Python 🧱

In Data Structures and Algorithms (DSA), arrays are the most fundamental linear data structures. Mastering arrays is crucial because a vast majority of algorithmic problems utilize them in some form.

---

### 1️⃣ What is a Static Array?

A **Static Array** is a container that stores a fixed number of elements of the same data type in contiguous (adjacent) memory locations. 

```
Memory Address:  1000   1004   1008   1012   1016
               ┌──────┬──────┬──────┬──────┬──────┐
Element:       │  10  │  20  │  30  │  40  │  50  │
               └──────┴──────┴──────┴──────┴──────┘
Index:             0      1      2      3      4
```

In low-level languages like C or C++, arrays must have a pre-declared size:
```cpp
int numbers[5] = {10, 20, 30, 40, 50}; // Fixed size of 5 integers
```

#### ⚡ Key Features of Static Arrays:
*   **Contiguous Memory:** Elements are placed next to each other in memory.
*   **Fixed Size:** The size of the array cannot be changed once it is allocated.
*   **Homogeneous Elements:** Every element must be of the exact same data type (e.g., all integers or all floats).
*   **Fast Random Access:** Using the formula `Address(arr[i]) = Base_Address + i * Size_of_Element`, we can access any element in $O(1)$ time.

---

### 2️⃣ What is a Dynamic List in Python?

Python does not have built-in support for low-level static arrays. Instead, it provides the **`list`** type, which is a **Dynamic Array** under the hood.

```python
# A Python list can change size and store heterogeneous types
my_list = [10, "Apple", 3.14, True]
```

#### 🔍 How Python Lists Work under the hood:
1.  **Array of References:** Instead of storing values directly in contiguous memory, a Python list stores **memory addresses (references)** pointing to the actual objects. This is how Python lists can store multiple data types.
2.  **Dynamic Resizing (Over-allocation):** When the list runs out of allocated slots, Python automatically allocates a larger block of memory (usually $1.125 \times \text{size} + 9$), copies the existing references to the new array, and deletes the old one.

#### ⚡ Key Features of Python Lists:
*   **Dynamic Size:** Can grow or shrink automatically as elements are added or removed.
*   **Heterogeneous:** Can store elements of different data types (integers, strings, custom objects) within the same list.
*   **Referential Memory:** Elements themselves are stored non-contiguously in memory, but the *pointers* to them are stored contiguously.

#### 📈 Mathematical Proof: Amortized $O(1)$ Insertion
Why is inserting at the end of a dynamic array $O(1)$ on average, even though a resize takes $O(n)$?
Imagine we start with an empty array of capacity 1. We insert $N$ elements sequentially, doubling the capacity each time it fills up.
* Resizes happen at sizes: $1, 2, 4, 8, \dots, 2^k$ (where $2^k \le N$).
* The cost of inserting an element without resizing is $1$ write operation.
* The cost of resizing is copying all existing elements, which takes $C$ operations when capacity is $C$.

Total work done for $N$ insertions:
$$\text{Total Work} = \text{Insertion Cost} + \text{Copying Cost}$$
$$\text{Total Work} = N + (1 + 2 + 4 + 8 + \dots + 2^k)$$

The second part is a geometric progression sum:
$$1 + 2 + 4 + \dots + 2^k = 2^{k+1} - 1 < 2N$$

So,
$$\text{Total Work} < N + 2N = 3N$$
$$\text{Amortized Cost per Insertion} = \frac{\text{Total Work}}{N} \approx \frac{3N}{N} = O(1)$$

> [!WARNING]
> **The Constant Factor Trap (Interview Question):**
> If capacity increases **geometrically** (e.g., doubling: $1 \to 2 \to 4 \to 8 \dots$), the amortized insertion time is **$O(1)$**.
> If capacity increases **arithmetically** (e.g., adding a fixed size $K$: $10 \to 20 \to 30 \to 40 \dots$), the total cost to insert $N$ elements is $O(N^2)$, making the amortized cost **$O(N)$**! Always explain this difference to the interviewer.

#### ⚠️ Python-Specific Interview Traps & Gotchas

##### Trap 1: Shallow Copy vs. Deep Copy in 2D Arrays
When duplicating a 2D array, using `.copy()` or list slicing `[:]` only copies the *outer* list. The inner lists still point to the same memory addresses.
```python
# ❌ BUG: Modifying copy modifies original
original = [[1, 2], [3, 4]]
shallow_copy = original.copy()

shallow_copy[0][0] = 99
print(original)  # Output: [[99, 2], [3, 4]] !!

# ✅ CORRECT: Deep Copy
import copy
deep_copy = copy.deepcopy(original)
# Or using list comprehension:
deep_copy = [[val for val in row] for row in original]
```

##### Trap 2: Default Mutable Argument Gotcha
Passing a mutable type (like a list) as a default parameter value in Python retains references across function calls.
```python
# ❌ BUG
def add_to_array(val, arr=[]):
    arr.append(val)
    return arr

print(add_to_array(1))  # Output: [1]
print(add_to_array(2))  # Output: [1, 2] (Should have been [2]!)

# ✅ CORRECT
def add_to_array(val, arr=None):
    if arr is None:
        arr = []
    arr.append(val)
    return arr
```

##### Trap 3: Creating a 2D Array using Multiplication `*`
```python
# ❌ BUG: All rows point to the exact same list object!
matrix = [[0] * 3] * 3
matrix[0][0] = 5
print(matrix)  # Output: [[5, 0, 0], [5, 0, 0], [5, 0, 0]] !!

# ✅ CORRECT: Nested list comprehension
matrix = [[0] * 3 for _ in range(3)]
```

---

### 3️⃣ Multidimensional Arrays (Matrices) 🗺️

A **Multidimensional Array** is an array of arrays. The most common type is a **2D Array** (often called a **Matrix**), which is structured as a grid with rows and columns.

```
       Column 0  Column 1  Column 2
Row 0:  [ 1,       2,        3 ]
Row 1:  [ 4,       5,        6 ]
Row 2:  [ 7,       8,        9 ]
```

#### 💡 Definition
A multidimensional array extends the concept of a standard 1D array to multiple dimensions. A 2D array represents a table (rows and columns), a 3D array represents a cube (height, width, depth), and $N$-D arrays represent higher-dimensional spaces.

#### 🐍 Representing 2D Arrays in Python
In Python, we represent a 2D array using a **Nested List** (a list containing other lists):

```python
# Creating a 3x3 2D list (Matrix)
matrix = [
    [1, 2, 3],  # Row 0
    [4, 5, 6],  # Row 1
    [7, 8, 9]   # Row 2
]

# Accessing Elements: matrix[row_index][column_index]
print(matrix[0][1])  # Output: 2 (Row 0, Column 1)
print(matrix[2][0])  # Output: 7 (Row 2, Column 0)
```

#### ⚙️ Memory Layout of Multidimensional Arrays
In lower-level languages, multidimensional arrays are stored in a linear 1D memory space using one of two mappings. Suppose we have a 2D array $A$ of dimensions $R \times C$ (Rows $\times$ Columns), starting at base memory address $\text{Base}$, and each element occupies $W$ bytes of space:

1.  **Row-Major Order (Common in C, C++, Python under the hood):** Elements are stored row-by-row consecutively.
    *   Linear sequence: $A[0][0], A[0][1], \dots, A[0][C-1], A[1][0], A[1][1], \dots$
    *   **Addressing Formula:**
        $$\text{Address}(A[i][j]) = \text{Base} + (i \times C + j) \times W$$
2.  **Column-Major Order (Common in Fortran, MATLAB):** Elements are stored column-by-column.
    *   Linear sequence: $A[0][0], A[1][0], \dots, A[R-1][0], A[0][1], A[1][1], \dots$
    *   **Addressing Formula:**
        $$\text{Address}(A[i][j]) = \text{Base} + (j \times R + i) \times W$$

> [!NOTE]
> Since Python uses an array of pointers, a nested list is a dynamic 2D structure where each sub-list can theoretically be of different lengths (often called a **Jagged Array**).

---

### ⚔️ Array/List vs. Linked List (The Classic Interview Comparison)

When designing systems or solving DSA problems, you must choose between Arrays and Linked Lists. Below is a comprehensive comparison:

| Metric | Array / Dynamic List | Linked List |
| :--- | :--- | :--- |
| **Memory Allocation** | Contiguous blocks in memory | Non-contiguous; nodes linked via pointers |
| **Random Access** | $O(1)$ (Direct access using index) | $O(n)$ (Must traverse node-by-node) |
| **Insertion/Deletion at End** | $O(1)$ amortized | $O(1)$ if tail pointer is maintained, else $O(n)$ |
| **Insertion/Deletion at Start** | $O(n)$ (Requires shifting elements) | $O(1)$ (Just update head pointers) |
| **Cache Locality** | **Excellent (Spatial Locality)** | **Poor** (Pointer-chasing across heap) |
| **Memory Overhead** | Minimal (Only array capacity overhead) | High (Requires storing pointers for every node) |

#### 🧠 Why Cache Locality Matters (Deep-Dive Interview Concept)
CPUs load memory into high-speed caches in chunks called **Cache Lines** (typically 64 bytes). 
* When you access `arr[0]`, the CPU loads the next few elements (`arr[1]`, `arr[2]`, etc.) into the cache automatically. This is called **spatial locality**, making linear scans of arrays incredibly fast.
* With a **Linked List**, nodes are allocated dynamically on the heap at arbitrary memory addresses. Traversing a linked list causes **Cache Misses** (pointer chasing), requiring the CPU to fetch from slower main RAM constantly.

---

### 4️⃣ Basic Operations in Array/List

Here are the core operations, their Python code, and their corresponding complexities.

### 1. Access Element – $O(1)$
Accessing an element is instantaneous if you know the index.
```python
arr = [10, 20, 30, 40]
element = arr[2]  # Returns 30 (Constant Time)
```

### 2. Insert Element
*   **At the End – $O(1)$ amortized:** Adding an element to the end.
    ```python
    arr.append(50)  # arr becomes [10, 20, 30, 40, 50]
    ```
*   **At the Beginning/Middle – $O(n)$:** Inserting requires shifting all subsequent elements to the right to make space.
    ```python
    arr.insert(0, 5)  # arr becomes [5, 10, 20, 30, 40, 50] (Shifts all elements)
    ```

### 3. Delete Element
*   **At the End – $O(1)$:** Removing the last element.
    ```python
    arr.pop()  # Removes and returns 50 (Fast)
    ```
*   **At the Beginning/Middle – $O(n)$:** Deleting requires shifting all subsequent elements to the left to fill the gap.
    ```python
    arr.pop(0)    # Removes index 0 (shifts all elements to the left)
    arr.remove(20) # Search for value 20 and remove it (requires shifting)
    ```

### 4. Traversal – $O(n)$
Visiting every element of the array.
```python
# 1D Array Traversal
for num in arr:
    print(num)

# 2D Array (Matrix) Traversal - O(R * C)
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        print(matrix[row][col], end=" ")
    print()
```

### 5. Searching
*   **Linear Search – $O(n)$:** Checking every element from start to finish.
    ```python
    if 30 in arr:
        print("Found")
    ```
*   **Binary Search – $O(\log n)$:** Splitting the search interval in half. Only works on **sorted** arrays.
    ```python
    import bisect
    index = bisect.bisect_left(arr, 30)  # O(log n)
    ```

---

# 5️⃣ Time Complexity Summary

| Operation | 1D Static Array | Python List (Dynamic) | 2D Array / Matrix ($R \times C$) |
| :--- | :--- | :--- | :--- |
| **Access by Index** | $O(1)$ | $O(1)$ | $O(1)$ |
| **Search (Linear)** | $O(n)$ | $O(n)$ | $O(R \times C)$ |
| **Insert at End** | N/A (Fixed size) | $O(1)$ amortized | $O(1)$ (append row) |
| **Insert at Index** | $O(n)$ | $O(n)$ | $O(R \times C)$ (shifting rows/columns)|
| **Delete from End** | N/A (Fixed size) | $O(1)$ | $O(1)$ |
| **Delete from Index**| $O(n)$ | $O(n)$ | $O(R \times C)$ |

---

# 6️⃣ Why Array/List is Important in DSA? (Interview Patterns)

Almost 50% of array-based interview problems can be categorized into 6 core algorithmic patterns. Mastering these is key to cracking coding rounds:

### 1. Two Pointers Pattern
*   **Technique:** Maintain two index pointers that move towards each other or in the same direction.
*   **When to use:** Array is sorted, or we need to compare elements from both ends (e.g., palindrome validation, meeting in the middle, reversing elements).
*   **Classic Problems:**
    *   [Two Sum II - Input array is sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
    *   [Container With Most Water](https://leetcode.com/problems/container-with-most-water/)
    *   [3Sum](https://leetcode.com/problems/3sum/)

### 2. Sliding Window Pattern
*   **Technique:** Maintain a continuous subarray (window) defined by `left` and `right` pointers that grows, shrinks, or slides based on constraints.
*   **When to use:** Finding contiguous subarrays with a specific condition (e.g., maximum sum, shortest length, unique characters).
*   **Classic Problems:**
    *   [Maximum Sum Subarray of Size K](https://practice.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1)
    *   [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
    *   [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)

### 3. Prefix Sum Pattern
*   **Technique:** Precompute a cumulative sum array where `prefix[i] = arr[0] + arr[1] + ... + arr[i]`. This allows range sum queries `sum(i, j)` to be calculated in $O(1)$ time: `prefix[j] - prefix[i-1]`.
*   **When to use:** Frequent range-sum queries, or finding subarrays with specific sums when combined with a Hash Map.
*   **Classic Problems:**
    *   [Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/)
    *   [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)

### 4. Kadane’s Algorithm (Dynamic Programming)
*   **Technique:** Track maximum subarray sum ending at current index: `curr_max = max(arr[i], curr_max + arr[i])`.
*   **When to use:** Finding the contiguous subarray with the largest sum.
*   **Classic Problems:**
    *   [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

### 5. Dutch National Flag (Three-Way Partitioning)
*   **Technique:** Maintain three pointers (`low`, `mid`, `high`) to partition an array into three groups in a single pass.
*   **When to use:** Sorting an array containing only three distinct keys/values (e.g., 0, 1, and 2).
*   **Classic Problems:**
    *   [Sort Colors](https://leetcode.com/problems/sort-colors/)

### 6. Subarrays vs. Subsequences vs. Subsets (Terminology Clarification)
This is a frequent source of confusion during interviews. Make sure you use the correct term:
*   **Subarray:** Contiguous elements (e.g., for `[1,2,3]`, `[1,2]` is a subarray, but `[1,3]` is not). Total subarrays = $O(N^2)$.
*   **Subsequence:** Elements in the same relative order, but not necessarily contiguous (e.g., `[1,3]` is a subsequence of `[1,2,3]`). Total subsequences = $2^N - 1$.
*   **Subset:** Any mathematical combination of elements, order does not matter (e.g., `{3,1}` is the same as `{1,3}`). Total subsets = $2^N$.

---

# 7️⃣ Example DSA Problems

### 💡 Problem 1: Find Maximum Element in a 1D Array
```python
def find_max(arr):
    if not arr:
        return None
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

# Test
print(find_max([5, 2, 9, 1, 7]))  # Output: 9
```
*   **Time Complexity:** $O(n)$
*   **Space Complexity:** $O(1)$

### 💡 Problem 2: Search in a Sorted 2D Matrix
Write an efficient algorithm that searches for a value in an $M \times N$ matrix. This matrix has properties:
1. Integers in each row are sorted from left to right.
2. The first integer of each row is greater than the last integer of the previous row.

```python
def search_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
        
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Treat 2D matrix as a flat 1D sorted array for Binary Search
    low = 0
    high = rows * cols - 1
    
    while low <= high:
        mid = (low + high) // 2
        # Map 1D index back to 2D coordinates
        mid_val = matrix[mid // cols][mid % cols]
        
        if mid_val == target:
            return True
        elif mid_val < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return False

# Test
matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
print(search_matrix(matrix, 3))   # Output: True
print(search_matrix(matrix, 15))  # Output: False
```
*   **Time Complexity:** $O(\log(R \times C))$ where $R$ is the number of rows and $C$ is the number of columns.
*   **Space Complexity:** $O(1)$

---

# 8️⃣ Curated Practice Problems Roadmap 🗺️

To master arrays and confidently solve any array-based question, practice these handpicked LeetCode problems categorized by pattern. They range from basic concepts to advanced interview questions and focus on teaching you the core strategy.

### 👥 1. Two Pointers
*   **Easy:** [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) — *Core idea: Meet in the middle.*
*   **Easy:** [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) — *Core idea: Read/write pointers moving in the same direction.*
*   **Medium:** [167. Two Sum II - Sorted Input](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) — *Core idea: Shrinking search space from both ends.*
*   **Medium:** [15. 3Sum](https://leetcode.com/problems/3sum/) — *Core idea: Sorting + Two Pointers + Duplicate handling.*
*   **Medium:** [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/) — *Core idea: Greedy pointer movement.*
*   **Hard:** [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) — *Core idea: Precomputed left/right max arrays or two-pointer space optimization.*

### 🪟 2. Sliding Window
*   **Easy:** [643. Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/) — *Core idea: Fixed-size window.*
*   **Medium:** [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) — *Core idea: Variable-size window using a Set for unique checks.*
*   **Medium:** [424. Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) — *Core idea: Variable-size window with character frequency tracking.*
*   **Hard:** [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) — *Core idea: Double pointer expansion/contraction using target maps.*

### 📊 3. Prefix Sum & Hashing
*   **Easy:** [724. Find Pivot Index](https://leetcode.com/problems/find-pivot-index/) — *Core idea: Sum comparison (total_sum vs. left_sum).*
*   **Medium:** [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) — *Core idea: Storing prefix sum frequencies in a Hash Map to find count of target sums in $O(N)$ time.*
*   **Medium:** [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) — *Core idea: Constructing prefix/suffix products without using division.*

### ⚡ 4. Dynamic Programming & Greedy (Kadane's)
*   **Easy:** [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) — *Core idea: Tracking minimum price so far to maximize profit.*
*   **Easy:** [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) — *Core idea: Kadane's algorithm (reset current sum to 0 if it goes negative).*
*   **Medium:** [152. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) — *Core idea: Tracking both min and max products due to double negatives.*

### 🏁 5. Array In-Place Modification (Index as Hash Key)
*   **Medium:** [75. Sort Colors](https://leetcode.com/problems/sort-colors/) — *Core idea: Dutch National Flag algorithm (3-pointer partitioning).*
*   **Medium:** [442. Find All Duplicates in an Array](https://leetcode.com/problems/find-all-duplicates-in-an-array/) — *Core idea: In-place marking (negating the value at index `abs(val)-1`). This achieves $O(N)$ time and $O(1)$ auxiliary space.*
*   **Hard:** [41. First Missing Positive](https://leetcode.com/problems/first-missing-positive/) — *Core idea: Cyclic sort (swapping elements to their correct index places).*

### 🗺️ 6. 2D Matrix / Grid Traversal
*   **Medium:** [74. Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/) — *Core idea: Treating 2D sorted matrix as 1D array.*
*   **Medium:** [54. Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) — *Core idea: Traversal with four shrinking boundaries.*
*   **Medium:** [48. Rotate Image](https://leetcode.com/problems/rotate-image/) — *Core idea: Matrix transposition followed by row reversal.*
*   **Medium:** [240. Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/) — *Core idea: Staircase search (starting from top-right or bottom-left corner).*

