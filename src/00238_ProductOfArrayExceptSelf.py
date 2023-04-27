# https://leetcode.com/problems/product-of-array-except-self/description/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums);

        productLeft = [0]*length;
        productRight = [0]*length;
        result = [0]*length;

        productLeft[0] = 1;
        productRight[length-1] = 1;

        for i in range(1, length):
            productLeft[i] = nums[i-1] * productLeft[i-1];

        for i in reversed(range(length-1)):
            productRight[i] = nums[i+1] * productRight[i+1];

        for i in range(length):
            result[i] = productLeft[i] * productRight[i];

        return result;