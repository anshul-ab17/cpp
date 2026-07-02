# Array + HashMap of indices sets.
import random
from collections import defaultdict

class RandomizedCollection:
    def __init__(self):
        self.vals = []
        self.idx = defaultdict(set)

    def insert(self, val):
        present = val in self.idx and len(self.idx[val]) > 0
        self.idx[val].add(len(self.vals))
        self.vals.append(val)
        return not present

    def remove(self, val):
        if not self.idx[val]:
            return False
        remove_idx = self.idx[val].pop()
        last_idx = len(self.vals) - 1
        last_val = self.vals[last_idx]

        self.vals[remove_idx] = last_val
        if remove_idx != last_idx:
            self.idx[last_val].add(remove_idx)
            self.idx[last_val].discard(last_idx)

        self.vals.pop()
        return True

    def getRandom(self):
        return random.choice(self.vals)
