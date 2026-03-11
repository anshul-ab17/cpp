# LC 752. Open the Lock | Medium
from collections import deque

class Solution:
    def openLock(self, deadends, target):
        dead = set(deadends)
        if '0000' in dead: return -1
        q = deque([('0000', 0)]); visited = {'0000'}
        while q:
            state, turns = q.popleft()
            if state == target: return turns
            for i in range(4):
                d = int(state[i])
                for move in [(d+1)%10, (d-1)%10]:
                    new = state[:i] + str(move) + state[i+1:]
                    if new not in visited and new not in dead:
                        visited.add(new); q.append((new, turns+1))
        return -1
