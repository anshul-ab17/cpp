# LC 528. Random Pick with Weight | Medium | Meta
import bisect, random

class Solution:
    def __init__(self, w):
        self.prefix = []
        total = 0
        for weight in w: total += weight; self.prefix.append(total)
        self.total = total

    def pickIndex(self):
        target = random.random() * self.total
        return bisect.bisect_right(self.prefix, target)
