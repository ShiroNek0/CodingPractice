import math

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if len(nums) == 0:
            return -1

        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1 

        pivot = searchPivot(nums, 0, len(nums)-1)
        first = searchBinary(nums, 0, pivot, target)
        if (first == -1):
            return searchBinary(nums, pivot+1, len(nums)-1, target)
        else:
            return first

def searchPivot(nums: list[int], start, end) -> int:
    if nums[start] <= nums[end]:
        return start-1
    else:
        check = math.floor((end+start)/2)
        if (nums[start] <= nums[check]):
            return searchPivot(nums, check+1, end)
        else:
            return searchPivot(nums, start, check)

def searchBinary(nums: list[int], left, right, target) -> int:
    while(left <= right):
        check = math.floor((right+left)/2)

        if (target == nums[check]):
            return check

        if (target < nums[check]):
            right = check - 1
        else:
            left = check + 1

    return -1