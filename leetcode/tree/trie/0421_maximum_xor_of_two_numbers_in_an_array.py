# Bitwise Trie.
# Insert all numbers bit by bit and greedily maximize XOR.
class Solution:
    def findMaximumXOR(self, nums):
        max_num = max(nums)
        bits = max_num.bit_length()
        root = {}

        for num in nums:
            node = root
            for i in range(bits - 1, -1, -1):
                bit = (num >> i) & 1
                node = node.setdefault(bit, {})

        best = 0
        for num in nums:
            node = root
            cur = 0
            for i in range(bits - 1, -1, -1):
                bit = (num >> i) & 1
                want = 1 - bit
                if want in node:
                    cur = (cur << 1) | 1
                    node = node[want]
                else:
                    cur = cur << 1
                    node = node[bit]
            best = max(best, cur)

        return best
