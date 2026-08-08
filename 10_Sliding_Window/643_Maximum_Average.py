# LeetCode 643: Maximum Average Subarray I
# Time Complexity: O(N)
# Space Complexity: O(1)

def findMaxAverage(nums: list[int], k: int) -> float:
    # Compute the sum of the first window of size k
    window_sum = sum(nums[:k])
    max_sum = window_sum
    
    # Slide the window across the array
    for i in range(k, len(nums)):
        # Slide: add the new element on the right, subtract the old element on the left
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)
        
    return max_sum / k

if __name__ == "__main__":
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    result = findMaxAverage(nums, k)
    print(f"Array: {nums}")
    print(f"Window Size (k): {k}")
    print(f"Maximum Average Subarray: {result} (Expected: 12.75)")
