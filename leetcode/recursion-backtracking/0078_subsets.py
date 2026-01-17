# LC 78. Subsets | Medium
class Solution:
    def subsets_iter(self, nums):
        res = [[]]
        for num in nums: res += [s + [num] for s in res]
        return res

    def subsets(self, nums):
        res = []
        def bt(start, path):
            res.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i]); bt(i + 1, path); path.pop()
        bt(0, []); return res
