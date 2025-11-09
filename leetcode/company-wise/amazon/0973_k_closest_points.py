# LC 973. K Closest Points to Origin | Medium | Amazon
import heapq

class Solution:
    def kClosest(self, points, k):
        return heapq.nsmallest(k, points, key=lambda p: p[0]**2 + p[1]**2)
