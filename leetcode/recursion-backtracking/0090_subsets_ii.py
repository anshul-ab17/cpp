class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        ans = []
        def dfs(i, cur):
            ans.append(cur[:])
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]: continue
                cur.append(nums[j])
                dfs(j+1, cur)
                cur.pop()
        dfs(0, [])
        return ans
