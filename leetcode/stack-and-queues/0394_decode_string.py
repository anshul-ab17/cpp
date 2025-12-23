class Solution:
    def decodeString(self, s):
        st = []
        for ch in s:
            if ch != ']':
                st.append(ch)
            else:
                cur = ''
                while st[-1] != '[':
                    cur = st.pop() + cur
                st.pop()
                k = ''
                while st and st[-1].isdigit():
                    k = st.pop() + k
                st.append(int(k) * cur)
        return ''.join(st)
