from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        groups = defaultdict(list)

        for s in strs:
            key = tuple(sorted(s))
            groups[key].append(s)

        return groups.values()
