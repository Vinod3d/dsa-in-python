def isTrionic( nums: List[int]) -> bool:
        n = len(nums)
        if n <4:
            return False
        phase = 0
        inc = 0

        for i in range(1, n):
            if nums[i] == nums[i-1]:
                return False
            
            if phase == 0:
                if nums[i] > nums[i - 1]:
                    inc+=1
                else:
                    if inc == 0:
                        return False
                    phase = 1
            
            elif phase == 1:
                if nums[i] > nums[i - 1]:
                    phase = 2
            else:
                if nums[i] < nums[i - 1]:
                    return False
        return phase == 2

# print(isTrionic([1, 3, 2, 4, 3]))  # Output: False
print(isTrionic([1, 3, 5, 4, 2, 6]))  