class Solution:
    def nextGreaterElement(self, nums1, nums2):
        st, nxt = [], {}
        for n in nums2:
            while st and st[-1] < n:
                nxt[st.pop()] = n
            st.append(n)
        return [nxt.get(x, -1) for x in nums1]
