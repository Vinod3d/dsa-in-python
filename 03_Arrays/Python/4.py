# 1299. Replace Elements with Greatest Element on Right Side
from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_right = -1

        # /* Brut force*/

        # for i in range(len(arr) - 1):
        #     max_val = 0
        #     for j in range(i + 1, len(arr)):
        #         if arr[j] > max_val:
        #             max_val = arr[j]
        #     arr[i] = max_val
        # arr[-1] = -1

        # Optimal solution

        for i in range(len(arr) - 1, -1, -1):
            current = arr[i]
            arr[i] = max_right
            if current > max_right:
              max_right = current


        return arr

# Example usage:
solution = Solution()
print(solution.replaceElements([17, 18, 5, 4, 6, 1]))  # Output: [18, 6, 6, 6, 1, -1]

