from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def recursion(curSub: List[int], nextIndex):
            if (nextIndex <= orgLen):
                resList.append(curSub)

            for i in range(nextIndex, orgLen):
                newSub = curSub[:]
                newSub.append(nums[i])
                recursion(newSub, i + 1)

        resList = []
        orgLen = len(nums)
        recursion([], 0)
        return resList