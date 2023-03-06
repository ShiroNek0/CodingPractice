# 1. Two Sum
# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {};
        for i in range(len(nums)):
            hashmap[nums[i]] = i;
        for j in range(len(nums)):
            complement = target - nums[j];
            if (complement in hashmap and hashmap[complement] != j):
                return [hashmap[target - nums[j]], j];

        return [];

