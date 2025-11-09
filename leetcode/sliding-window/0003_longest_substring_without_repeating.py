# LC 3. Longest Substring Without Repeating Characters | Medium
class Solution:
    def lengthOfLongestSubstring_brute(self, s):
        res = 0
        for i in range(len(s)):
            seen = set()
            for j in range(i, len(s)):
                if s[j] in seen: break
                seen.add(s[j]); res = max(res, j - i + 1)
        return res

    # Sliding window - O(n)
    def lengthOfLongestSubstring(self, s):
        seen = {}; l = res = 0
        for r, ch in enumerate(s):
            if ch in seen and seen[ch] >= l:
                l = seen[ch] + 1
            seen[ch] = r; res = max(res, r - l + 1)
        return res
