# 414. Second, Third Maximum Number


from ast import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # Brut force
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if nums[i] < nums[j]:
        #             nums[i], nums[j] = nums[j], nums[i]
        # if n < 3:
        #     return nums[0]
        # return nums[2]
    

        # Optimal solution using set and sorting
        # unique_nums = list(set(nums))
        # unique_nums.sort(reverse=True)
        # if len(unique_nums) < 3:
        #     return unique_nums[0]
        # return unique_nums[2]
    
        # optimal solution without in built sort function
        unique_nums = list(set(nums))
        first = second = third = float('-inf')
        for num in unique_nums:
            if num > first:
                third = second
                second = first
                first = num
            elif first > num > second:
                third = second
                second = num
            elif second > num > third:
                third = num
    


Solution = Solution()
print(Solution.thirdMax([3, 2, 12, 8, 7, 23, 14]))  # Output: 1