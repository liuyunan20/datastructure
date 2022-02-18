class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        profits = [0]
        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            profits.append(prices[i] - min_price)
        max_profit = max(profits) 
        return max_profit
