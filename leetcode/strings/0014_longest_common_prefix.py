# LC 14. Longest Common Prefix | Easy
class Solution:
    def longestCommonPrefix_brute(self, strs):
        if not strs: return ""
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
        return prefix

    # Vertical scanning
    def longestCommonPrefix(self, strs):
        if not strs: return ""
        for i, ch in enumerate(strs[0]):
            for s in strs[1:]:
                if i >= len(s) or s[i] != ch:
                    return strs[0][:i]
        return strs[0]

    # Python-specific: zip
    def longestCommonPrefix_zip(self, strs):
        res = []
        for chars in zip(*strs):
            if len(set(chars)) == 1: res.append(chars[0])
            else: break
        return "".join(res)
