class Solution:
    def maxProduct(self, words):
        masks = []
        for w in words:
            mask = 0
            for ch in w:
                mask |= 1 << (ord(ch) - ord('a'))
            masks.append(mask)

        ans = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if masks[i] & masks[j] == 0:
                    ans = max(ans, len(words[i]) * len(words[j]))

        return ans
