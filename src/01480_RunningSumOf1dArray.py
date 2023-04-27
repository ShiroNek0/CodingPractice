# 1480. Running Sum of 1d Array
# https://leetcode.com/problems/running-sum-of-1d-array/description/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = [];
        previous = 0;

        for i in range(len(nums)):
            result.append(nums[i]+previous);
            previous =  result[i];

        return result;