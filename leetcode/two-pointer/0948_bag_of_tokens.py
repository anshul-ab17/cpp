class Solution:
    def bagOfTokensScore(self, tokens, power):
        tokens.sort()
        l, r, score, ans = 0, len(tokens)-1, 0, 0
        while l <= r:
            if power >= tokens[l]:
                power -= tokens[l]; score += 1; l += 1
                ans = max(ans, score)
            elif score:
                power += tokens[r]; score -= 1; r -= 1
            else: break
        return ans
