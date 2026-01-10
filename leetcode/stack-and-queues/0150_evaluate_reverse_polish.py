# LC 150. Evaluate Reverse Polish Notation | Medium
class Solution:
    def evalRPN(self, tokens):
        stack = []
        ops = {'+': lambda a,b: a+b, '-': lambda a,b: a-b,
               '*': lambda a,b: a*b, '/': lambda a,b: int(a/b)}
        for t in tokens:
            if t in ops:
                b, a = stack.pop(), stack.pop()
                stack.append(ops[t](a, b))
            else: stack.append(int(t))
        return stack[0]
