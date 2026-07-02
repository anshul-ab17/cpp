# Hard: BFS/Backtracking.
class Solution:
    def removeInvalidParentheses(self, s):
        def is_valid(string):
            bal = 0
            for ch in string:
                if ch == '(':
                    bal += 1
                elif ch == ')':
                    bal -= 1
                    if bal < 0:
                        return False
            return bal == 0

        level = {s}
        while True:
            valid = [x for x in level if is_valid(x)]
            if valid:
                return valid
            next_level = set()
            for x in level:
                for i in range(len(x)):
                    if x[i] in "()":
                        next_level.add(x[:i] + x[i + 1:])
            level = next_level
