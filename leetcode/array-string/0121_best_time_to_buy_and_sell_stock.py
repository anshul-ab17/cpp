class Solution:
    def maxProfit(self, prices):
        buy = prices[0]
        profit = 0

        for price in prices:
            buy = min(buy, price)      # cheapest stock so far
            profit = max(profit, price - buy)

        return profit
