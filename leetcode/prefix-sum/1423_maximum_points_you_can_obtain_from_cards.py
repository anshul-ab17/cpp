class Solution:
    def maxScore(self, cards, k):
        total = sum(cards)
        window = len(cards) - k

        if window == 0:
            return total

        cur = sum(cards[:window])
        mn = cur

        for i in range(window, len(cards)):
            cur += cards[i] - cards[i-window]
            mn = min(mn, cur)

        return total - mn
