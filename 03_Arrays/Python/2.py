# 1672. Richest Customer Wealth
from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for customer in accounts:
            wealth = sum(customer)
            max_wealth = max(max_wealth, wealth)
        return max_wealth


solution = Solution()
print(solution.maximumWealth([[1,2,3],[3,2,1, 4]]))