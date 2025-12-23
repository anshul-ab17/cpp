class Solution:
    def largestRectangleArea(self, heights):
        st, ans = [], 0
        heights.append(0)
        for i, h in enumerate(heights):
            while st and heights[st[-1]] > h:
                H = heights[st.pop()]
                W = i if not st else i - st[-1] - 1
                ans = max(ans, H * W)
            st.append(i)
        return ans
