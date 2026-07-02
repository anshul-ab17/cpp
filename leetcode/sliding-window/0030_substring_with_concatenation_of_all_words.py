# Hard problem: use hashmap + fixed-size sliding windows.
from collections import Counter

class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        wlen = len(words[0])
        wcount = len(words)
        total = wlen * wcount
        need = Counter(words)
        res = []

        for offset in range(wlen):
            left = offset
            count = 0
            window = Counter()
            for right in range(offset, len(s) - wlen + 1, wlen):
                word = s[right:right + wlen]
                if word in need:
                    window[word] += 1
                    count += 1
                    while window[word] > need[word]:
                        lword = s[left:left + wlen]
                        window[lword] -= 1
                        count -= 1
                        left += wlen
                    if count == wcount:
                        res.append(left)
                        lword = s[left:left + wlen]
                        window[lword] -= 1
                        count -= 1
                        left += wlen
                else:
                    window.clear()
                    count = 0
                    left = right + wlen

        return res


if __name__ == "__main__":
    assert sorted(Solution().findSubstring("barfoothefoobarman", ["foo", "bar"])) == [0, 9]
