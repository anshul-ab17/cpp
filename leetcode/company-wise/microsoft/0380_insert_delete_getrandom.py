# LC 380. Insert Delete GetRandom O(1) | Medium | Microsoft
import random

class RandomizedSet:
    def __init__(self): self.lst = []; self.idx = {}
    def insert(self, val):
        if val in self.idx: return False
        self.idx[val] = len(self.lst); self.lst.append(val); return True
    def remove(self, val):
        if val not in self.idx: return False
        last = self.lst[-1]; i = self.idx[val]
        self.lst[i] = last; self.idx[last] = i
        self.lst.pop(); del self.idx[val]; return True
    def getRandom(self): return random.choice(self.lst)
