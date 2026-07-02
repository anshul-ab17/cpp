# Merge Sort or Segment Tree.
class Solution:
    def reversePairs(self, nums):
        def sort(lo, hi):
            if hi - lo <= 1:
                return 0
            mid = (lo + hi) // 2
            count = sort(lo, mid) + sort(mid, hi)

            j = mid
            for i in range(lo, mid):
                while j < hi and nums[i] > 2 * nums[j]:
                    j += 1
                count += j - mid

            nums[lo:hi] = sorted(nums[lo:hi])
            return count

        return sort(0, len(nums))
