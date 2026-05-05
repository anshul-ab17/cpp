# LC 787. Cheapest Flights Within K Stops | Medium (DP on Graph / Bellman-Ford)
class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        prices = [float('inf')] * n; prices[src] = 0
        for _ in range(k + 1):
            tmp = prices[:]
            for u, v, w in flights:
                if prices[u] != float('inf'):
                    tmp[v] = min(tmp[v], prices[u] + w)
            prices = tmp
        return prices[dst] if prices[dst] != float('inf') else -1
