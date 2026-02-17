
# 1732. Find the Highest Altitude
from typing import List

class Solution:
    def HighestAltitude(self, gain: List[int]) -> int:
        highest_altitude = 0
        current_altitude = 0
        for g in gain:
            current_altitude += g

            if current_altitude > highest_altitude:
                highest_altitude = current_altitude
        return highest_altitude
    

solution = Solution()
print(solution.HighestAltitude([-5,1,5,0,-7]))  # Output