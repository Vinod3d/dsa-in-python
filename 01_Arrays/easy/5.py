# 217. Contains Duplicate

from ast import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Brut force
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return True
        return False
    
        # Optimal solution by converting array value to index only if the value is positive and less than the length of the array

        # # Step 1: Find maximum value manually
        # max_val = nums[0]
        # i = 1
        # while i < len(nums):
        #     if nums[i] > max_val:
        #         max_val = nums[i]
        #     i += 1
        
        # # Step 2: Create new array of size max_val + 1
        # check = [0] * (max_val + 1)
        
        # # Step 3: Use value as index
        # i = 0
        # while i < len(nums):
        #     value = nums[i]
            
        #     if check[value] == 1:
        #         return True
            
        #     check[value] = 1
        #     i += 1
        
        # return False


        # Optimal solution using set

        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         return True
        #     seen.add(num)
        # return False

        # more optimal solution using set comprehension
        # return len(set(nums)) != len(nums)
    
# Example usage:
solution = Solution()
print(solution.containsDuplicate([1, 2, 3, 4]))  # Output