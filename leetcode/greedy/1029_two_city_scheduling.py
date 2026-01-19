class Solution:
    def twoCitySchedCost(self, costs):
        costs.sort(key=lambda x: x[0] - x[1])
        n = len(costs)//2
        return sum(a for a,b in costs[:n]) + sum(b for a,b in costs[n:])
