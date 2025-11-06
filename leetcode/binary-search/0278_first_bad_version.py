class Solution:
    def firstBadVersion(self, n):
        l, r = 1, n

        while l < r:
            m = (l + r) // 2

            if isBadVersion(m):
                r = m      # first bad may still be m
            else:
                l = m + 1

        return l
