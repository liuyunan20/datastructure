class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        n = len(prices)
        current = prices[0]
        result = 0
        while i < n:
            if prices[i] < current:
                current = prices[i]
                i += 1

            elif i + 1 < n and prices[i] > prices[i + 1]:
                result += prices[i] - current
                current = prices[i]
                i += 1

            elif i == n - 1:
                result += prices[i] - current
                i += 1
            else:
                i += 1
        return result
