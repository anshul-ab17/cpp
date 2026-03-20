class Solution:
    def removeKdigits(self, num, k):
        st = []

        for d in num:
            while st and k and st[-1] > d:
                st.pop()
                k -= 1
            st.append(d)

        while k:
            st.pop()
            k -= 1

        return ''.join(st).lstrip('0') or '0'
