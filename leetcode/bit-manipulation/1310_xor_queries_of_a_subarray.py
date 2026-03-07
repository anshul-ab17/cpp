class Solution:
    def xorQueries(self, arr, queries):
        pref = [0]
        for n in arr:
            pref.append(pref[-1] ^ n)

        return [pref[r + 1] ^ pref[l] for l, r in queries]
