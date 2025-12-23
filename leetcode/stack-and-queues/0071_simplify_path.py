class Solution:
    def simplifyPath(self, path):
        st = []
        for part in path.split('/'):
            if part in ('', '.'):
                continue
            if part == '..':
                if st: st.pop()
            else:
                st.append(part)
        return '/' + '/'.join(st)
