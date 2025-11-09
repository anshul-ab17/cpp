# LC 460. LFU Cache | Hard | Netflix
from collections import defaultdict, OrderedDict

class LFUCache:
    def __init__(self, capacity):
        self.cap = capacity; self.min_freq = 0
        self.key_val = {}; self.key_freq = {}
        self.freq_keys = defaultdict(OrderedDict)

    def get(self, key):
        if key not in self.key_val: return -1
        self._update(key); return self.key_val[key]

    def put(self, key, value):
        if self.cap <= 0: return
        if key in self.key_val: self.key_val[key] = value; self._update(key); return
        if len(self.key_val) >= self.cap:
            evict, _ = self.freq_keys[self.min_freq].popitem(last=False)
            del self.key_val[evict]; del self.key_freq[evict]
        self.key_val[key] = value; self.key_freq[key] = 1
        self.freq_keys[1][key] = None; self.min_freq = 1

    def _update(self, key):
        freq = self.key_freq[key]
        del self.freq_keys[freq][key]
        if not self.freq_keys[freq] and freq == self.min_freq: self.min_freq += 1
        self.key_freq[key] = freq + 1
        self.freq_keys[freq + 1][key] = None
