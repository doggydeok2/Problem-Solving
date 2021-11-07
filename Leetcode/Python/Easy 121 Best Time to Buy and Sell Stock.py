class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_value, max_profit = 0, 0
        
        for i in range(len(prices) - 1, -1, -1):
            max_value = max(max_value, prices[i])
            max_profit = max(max_value - prices[i], max_profit)
        
        return max_profit