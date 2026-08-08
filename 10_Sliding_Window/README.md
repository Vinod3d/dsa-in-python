# 🪟 The Sliding Window Pattern

Welcome to the **Sliding Window** pattern guide! This is one of the most powerful and frequently asked algorithmic patterns in coding interviews (LeetCode, FAANG). 

By the end of this guide, you will understand:
1. The core intuition of the sliding window.
2. How to identify when to use it.
3. The difference between **Fixed** and **Variable** windows.
4. How to implement them in both **Python** and **C++** with visual traces.

---

## 💡 The Core Intuition: What is a Sliding Window?

Imagine you are looking at a long train through a small, fixed-size passenger window that only lets you see **3 train cars at a time**. 

As the train moves forward:
- A new car enters your view from the right.
- An old car exits your view from the left.
- **You don't need to re-examine the cars in the middle**; they remain in your view.

In programming, the **Sliding Window** pattern is used to perform operations on a contiguous sequence (subarrays or substrings) without re-evaluating the overlapping elements.

### 🚀 Bruteforce vs. Sliding Window Complexity

Let's say we have an array of size $N$ and we want to find the maximum sum of $K$ consecutive elements.

| Approach | How it Works | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- |
| **Brute Force** | For *every* starting index, loop $K$ times to calculate the sum. | **$O(N \times K)$** | **$O(1)$** |
| **Sliding Window** | Compute the sum of the first window. Slide the window by subtracting the left element and adding the right element. | **$O(N)$** *(Only one pass)* | **$O(1)$** |

---

## 🔍 How to Identify Sliding Window Problems

Look for these key patterns in the problem description:
1. **Data Structure:** The input is a linear structure like an **Array**, **String**, or **Linked List**.
2. **Contiguous Elements:** The problem mentions **contiguous subarrays** or **substrings** (elements must be adjacent, no skipping!).
3. **Goal:** You are asked to find:
   - The *longest*, *shortest*, or *maximum/minimum* subarray/substring.
   - A subsegment meeting a specific criteria (e.g., target sum, no repeating characters).
4. **Keywords:** Look for words like `"window"`, `"contiguous"`, `"subarray of size K"`, `"consecutive"`, or `"substring"`.

---

## 🛠️ Category 1: Fixed-Size Sliding Window

In this category, the size of the window ($K$) is constant throughout the entire array traversal.

### 📌 Problem Example: LeetCode 643. Maximum Average Subarray I
> Given an array `nums` consisting of `n` elements, find a contiguous subarray of size `k` that has the maximum average value, and return this value.

#### 🚶 Step-by-Step Visualization
Let `nums = [1, 12, -5, -6, 50, 3]` and `k = 4`.

```text
Step 1: Build the first window of size k = 4 (indices 0 to 3)
[ 1,  12, -5, -6 ] 50,  3
  L            R              -> Window Sum = 1 + 12 + (-5) + (-6) = 2
                                 Max Sum = 2

Step 2: Slide the window right. 
- Subtract nums[0] (left element leaving the window: 1)
- Add nums[4] (right element entering the window: 50)
1, [ 12, -5, -6,  50 ] 3
      L            R          -> Window Sum = 2 - 1 + 50 = 51
                                 Max Sum = max(2, 51) = 51

Step 3: Slide the window right. 
- Subtract nums[1] (12)
- Add nums[5] (3)
1, 12, [ -5, -6,  50,  3 ]
           L            R     -> Window Sum = 51 - 12 + 3 = 42
                                 Max Sum = max(51, 42) = 51

Result: Max Average = Max Sum / k = 51 / 4 = 12.75
```

---

#### 🐍 Python Implementation
```python
def findMaxAverage(nums: list[int], k: int) -> float:
    # 1. Calculate sum of the first window
    window_sum = sum(nums[:k])
    max_sum = window_sum
    
    # 2. Slide the window from index k to the end of the array
    for i in range(k, len(nums)):
        # Subtract the element going out, add the element coming in
        window_sum += nums[i] - nums[i - k]
        # Update the maximum sum encountered so far
        max_sum = max(max_sum, window_sum)
        
    return max_sum / k
```

#### 🦀 C++ Implementation
```cpp
#include <vector>
#include <numeric>
#include <algorithm>

double findMaxAverage(std::vector<int>& nums, int k) {
    // 1. Calculate sum of the first window
    double windowSum = std::accumulate(nums.begin(), nums.begin() + k, 0.0);
    double maxSum = windowSum;

    // 2. Slide the window
    for (int i = k; i < nums.size(); ++i) {
        windowSum += nums[i] - nums[i - k];
        maxSum = std::max(maxSum, windowSum);
    }

    return maxSum / k;
}
```

---

## 🛠️ Category 2: Variable-Size Sliding Window

In this category, the size of the window is **not fixed**. The window expands and contracts dynamically based on constraints.

### 📌 Problem Example: LeetCode 209. Minimum Size Subarray Sum
> Given an array of positive integers `nums` and a positive integer `target`, return the minimal length of a contiguous subarray of which the sum is $\ge$ `target`. If there is no such subarray, return `0` instead.

#### 🚶 Step-by-Step Template Strategy
1. **Expand** the window by moving the `right` pointer (add `nums[right]` to sum).
2. **Shrink** the window from the left by moving the `left` pointer as long as the window condition is still satisfied (`sum >= target`). Record the minimum window length during this shrink phase.

```text
Let nums = [2, 3, 1, 2, 4, 3] and target = 7.

R = 0: sum = 2  (< 7) -> Expand
R = 1: sum = 5  (< 7) -> Expand
R = 2: sum = 6  (< 7) -> Expand
R = 3: sum = 8  (>= 7) -> Valid!
       [2, 3, 1, 2], 4, 3  (Length = 4)
        L        R
       Shrink L -> sum becomes 8 - 2 = 6 (< 7). L moves to 1.
       
R = 4: sum = 6 + 4 = 10 (>= 7) -> Valid!
       2, [3, 1, 2, 4], 3  (Length = 4)
           L        R
       Shrink L -> sum becomes 10 - 3 = 7 (>= 7). L moves to 2.
       2, 3, [1, 2, 4], 3  (Length = 3, Update Min Length = 3)
              L     R
       Shrink L -> sum becomes 7 - 1 = 6 (< 7). L moves to 3.

R = 5: sum = 6 + 3 = 9 (>= 7) -> Valid!
       2, 3, 1, [2, 4, 3]  (Length = 3)
                 L     R
       Shrink L -> sum becomes 9 - 2 = 7 (>= 7). L moves to 4.
       2, 3, 1, 2, [4, 3]  (Length = 2, Update Min Length = 2)
                    L  R
       Shrink L -> sum becomes 7 - 4 = 3 (< 7). L moves to 5.

Result: Minimum length is 2 (subarray [4, 3]).
```

---

#### 🐍 Python Implementation
```python
def minSubArrayLen(target: int, nums: list[int]) -> int:
    left = 0
    window_sum = 0
    min_length = float('inf')
    
    # Expand window using the right pointer
    for right in range(len(nums)):
        window_sum += nums[right]
        
        # Shrink window as long as the condition is satisfied
        while window_sum >= target:
            min_length = min(min_length, right - left + 1)
            window_sum -= nums[left]
            left += 1
            
    return min_length if min_length != float('inf') else 0
```

#### 🦀 C++ Implementation
```cpp
#include <vector>
#include <algorithm>
#include <climits>

int minSubArrayLen(int target, std::vector<int>& nums) {
    int left = 0;
    int windowSum = 0;
    int minLength = INT_MAX;

    for (int right = 0; right < nums.size(); ++right) {
        windowSum += nums[right];

        // Shrink the window from the left
        while (windowSum >= target) {
            minLength = std::min(minLength, right - left + 1);
            windowSum -= nums[left];
            left++;
        }
    }

    return minLength == INT_MAX ? 0 : minLength;
}
```

---

## 📝 Sliding Window Cheat Sheet

| Feature | Fixed-Size Window | Variable-Size Window |
| :--- | :--- | :--- |
| **Window Width** | Stays constant (`k`) | Changes dynamically |
| **Pointers** | Usually one pointer `i` (using `i - k` to reference left) | Two pointers (`left` and `right`) |
| **Loop Structure** | Build first window, then a single loop from `k` to `n` | Outer loop expands `right`, inner `while` loops shrinks `left` |
| **Standard Goal** | Max sum, Max average, unique counts of length `K` | Longest/Shortest subarray satisfying a condition |

---

## 🎯 Recommended Practice Problems

Here are the best LeetCode problems to practice, sorted by difficulty:

### 🟢 Easy
1. [643. Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/) (Fixed)
2. [219. Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/) (Fixed)

### 🟡 Medium
3. [209. Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) (Variable)
4. [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) (Variable)
5. [438. Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) (Fixed)
6. [1004. Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/) (Variable)

### 🔴 Hard
7. [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) (Variable - Classic!)
8. [239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) (Fixed - Monotonic Queue)
