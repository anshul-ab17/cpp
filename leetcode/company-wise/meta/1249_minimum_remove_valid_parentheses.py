# LC 1249. Minimum Remove to Make Valid Parentheses | Medium | Meta
class Solution:
    def minRemoveToMakeValid(self, s):
        s = list(s); stack = []
        for i, ch in enumerate(s):
            if ch == '(': stack.append(i)
            elif ch == ')':
                if stack: stack.pop()
                else: s[i] = ''
        for i in stack: s[i] = ''
        return ''.join(s)
