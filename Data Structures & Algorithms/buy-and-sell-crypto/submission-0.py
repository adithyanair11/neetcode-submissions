class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_value = prices[0]

        for i in range(len(prices)):
           min_value = min(min_value, prices[i])

           profit = prices[i] - min_value

           max_profit = max(profit, max_profit)
        
        return max_profit
