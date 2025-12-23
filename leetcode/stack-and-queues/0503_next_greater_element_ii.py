class Solution:
    def nextGreaterElements(self, nums):
        n = len(nums)
        ans = [-1] * n
        st = []
        for i in range(2*n):
            while st and nums[st[-1]] < nums[i % n]:
                ans[st.pop()] = nums[i % n]
            if i < n:
                st.append(i)
        return ans
