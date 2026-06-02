# LeetCode #26 – Remove Duplicates from Sorted Array

# Skills you learn
# Two pointer technique
# In-place array modification
# O(n) time complexity
# O(1) space complexity

def removeDuplicates(nums):
    if not nums:
        return 0
    
    i = 0
    
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    
    return i + 1
    
# Example usage
nums = [1, 1, 2]
result = removeDuplicates(nums)
print(f"Length of array with unique elements: {result}")
print(f"Array with unique elements: {nums[:result]}")