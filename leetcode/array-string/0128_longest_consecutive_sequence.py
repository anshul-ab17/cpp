class Solution:
    def longestConsecutive(self, nums):
        st = set(nums)
        ans = 0

        for n in st:
            if n - 1 not in st:
                cur = n
                length = 1

                while cur + 1 in st:
                    cur += 1
                    length += 1

                ans = max(ans, length)

        return ans
