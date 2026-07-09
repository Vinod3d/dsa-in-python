# 1295. Find Numbers with Even Number of Digits

from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                count += 1
        return count

# Example usage:
solution = Solution()
print(solution.findNumbers([12, 345, 2, 6, 7896]))  # Output: 2


