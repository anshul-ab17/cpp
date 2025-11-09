# LC 716. Max Stack | Hard | Bloomberg
from sortedcontainers import SortedList

class MaxStack:
    def __init__(self):
        self.stack = SortedList(key=lambda x: x[1])
        self.vals = SortedList()
        self.cnt = 0

    def push(self, x):
        self.stack.add((self.cnt, x)); self.vals.add((x, self.cnt)); self.cnt += 1

    def pop(self):
        idx, val = self.stack.pop()
        self.vals.remove((val, idx)); return val

    def top(self): return self.stack[-1][1]

    def peekMax(self): return self.vals[-1][0]

    def popMax(self):
        val, idx = self.vals.pop()
        self.stack.remove((idx, val)); return val
