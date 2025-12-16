from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, s):
        heap = [(-v, k) for k, v in Counter(s).items()]
        heapq.heapify(heap)
        prev = (0, '')
        ans = []
        while heap:
            cnt, ch = heapq.heappop(heap)
            ans.append(ch)
            if prev[0] < 0:
                heapq.heappush(heap, prev)
            prev = (cnt + 1, ch)
        return ''.join(ans) if len(ans) == len(s) else ""
