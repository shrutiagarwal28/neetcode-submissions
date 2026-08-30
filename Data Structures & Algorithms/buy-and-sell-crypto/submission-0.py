class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0 
        min_buy = 0

        for i in range(1,len(prices)):
            profit = prices[i] - prices[min_buy]
            maxProfit = max(maxProfit, profit)

            if prices[i] < prices[min_buy]:
                min_buy = i
        
        return maxProfit