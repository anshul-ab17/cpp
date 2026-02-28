class Solution:
    def findComplement(self, num):
        mask = 1
        while mask <= num:
            mask <<= 1
        return (mask - 1) ^ num
