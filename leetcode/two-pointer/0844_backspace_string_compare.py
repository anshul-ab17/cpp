class Solution:
    def backspaceCompare(self, s, t):
        def build(x):
            st = []
            for c in x:
                if c == '#':
                    if st: st.pop()
                else: st.append(c)
            return st
        return build(s) == build(t)
