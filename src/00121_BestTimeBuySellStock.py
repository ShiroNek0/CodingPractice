# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf');
        maxProfit = 0;

        for i in range(len(prices)):
            if (prices[i] < minPrice):
                minPrice = prices[i];
            elif (maxProfit < prices[i] - minPrice):
                maxProfit = prices[i] - minPrice;

        return int(maxProfit);