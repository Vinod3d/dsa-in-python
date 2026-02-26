from ast import List


def buildArray(nums: List[int]):
        ans = []
        for i in range(len(nums)):

            ans.append(nums[nums[i]])


        print(ans)

buildArray([0,2,1,5,3,4]) #Output: [0,1,2,4,5,3]