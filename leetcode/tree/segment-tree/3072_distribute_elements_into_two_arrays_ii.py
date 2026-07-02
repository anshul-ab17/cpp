# Fenwick Tree counts with coordinate compression.
class Fenwick:
    def __init__(self, n):
        self.tree = [0] * (n + 1)

    def update(self, i, delta=1):
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & (-i)

    def query(self, i):
        total = 0
        while i > 0:
            total += self.tree[i]
            i -= i & (-i)
        return total

class Solution:
    def resultArray(self, nums):
        sorted_unique = sorted(set(nums))
        rank = {v: i + 1 for i, v in enumerate(sorted_unique)}
        m = len(sorted_unique)

        fen1 = Fenwick(m)
        fen2 = Fenwick(m)

        arr1, arr2 = [nums[0]], [nums[1]]
        fen1.update(rank[nums[0]])
        fen2.update(rank[nums[1]])

        for num in nums[2:]:
            r = rank[num]
            greater1 = len(arr1) - fen1.query(r)
            greater2 = len(arr2) - fen2.query(r)

            if greater1 > greater2:
                arr1.append(num)
                fen1.update(r)
            elif greater2 > greater1:
                arr2.append(num)
                fen2.update(r)
            elif len(arr1) <= len(arr2):
                arr1.append(num)
                fen1.update(r)
            else:
                arr2.append(num)
                fen2.update(r)

        return arr1 + arr2
