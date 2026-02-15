class MapSum:
    def __init__(self):
        self.mp = {}

    def insert(self, key, val):
        self.mp[key] = val

    def sum(self, prefix):
        return sum(v for k, v in self.mp.items() if k.startswith(prefix))
