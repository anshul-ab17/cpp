# Next Smaller Element.
class Solution:
    def finalPrices(self, prices):
        res = prices[:]
        stack = []

        for i, p in enumerate(prices):
            while stack and prices[stack[-1]] >= p:
                j = stack.pop()
                res[j] -= p
            stack.append(i)

        return res
