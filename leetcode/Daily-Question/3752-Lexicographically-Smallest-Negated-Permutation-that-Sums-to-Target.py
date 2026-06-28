class Solution:
    def lexSmallestNegatedPerm(self, n: int, target: int) -> list[int]:
        S = n * (n + 1) // 2

        if (S - target) < 0 or (S - target) % 2 != 0:
            return []

        sumPNeg = (S - target) // 2

        if sumPNeg < 0 or sumPNeg > S:
            return []

        pNegSet = set()
        curr_sum = 0

        for v in range(n, 0, -1):
            if curr_sum + v <= sumPNeg:
                curr_sum += v
                pNegSet.add(v)

        if curr_sum != sumPNeg:
            pNegSet = set()
            rem = sumPNeg

            for v in range(n, 0, -1):
                if rem >= v:
                    rem -= v
                    pNegSet.add(v)

        pPosSet = set(range(1, n + 1)) - pNegSet

        pNegList = sorted(pNegSet, reverse=True)
        pPosList = sorted(pPosSet, reverse=True)

        result = []

        for _ in range(n):
            candidateNeg = float('inf')
            if pNegList:
                candidateNeg = -pNegList[0]

            candidatePos = float('inf')
            if pPosList:
                candidatePos = pPosList[-1]

            if candidateNeg <= candidatePos:
                result.append(candidateNeg)
                pNegList.pop(0)
            else:
                result.append(candidatePos)
                pPosList.pop()

        return result
