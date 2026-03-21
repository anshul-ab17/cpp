# Min Heap Implementation
class MinHeap:
    def __init__(self): self.heap = []
    def push(self, val):
        self.heap.append(val); self._up(len(self.heap)-1)
    def pop(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        val = self.heap.pop()
        if self.heap: self._down(0)
        return val
    def _up(self, i):
        while i > 0:
            p = (i-1)//2
            if self.heap[i] < self.heap[p]: self.heap[i], self.heap[p] = self.heap[p], self.heap[i]; i = p
            else: break
    def _down(self, i):
        n = len(self.heap)
        while 2*i+1 < n:
            ch = 2*i+1
            if ch+1 < n and self.heap[ch+1] < self.heap[ch]: ch += 1
            if self.heap[i] <= self.heap[ch]: break
            self.heap[i], self.heap[ch] = self.heap[ch], self.heap[i]; i = ch

if __name__ == "__main__":
    h = MinHeap()
    for v in [5,3,8,1,2]: h.push(v)
    assert h.pop() == 1; assert h.pop() == 2; print("MinHeap OK")
