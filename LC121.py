class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 0
        maxProfit = 0
        while r < len(prices):
            buy = prices[l]
            sell = prices[r]
            profit = sell - buy
            maxProfit = max(maxProfit, profit)
            if buy > sell:
                l = r
            else:
                r += 1
        return maxProfit
