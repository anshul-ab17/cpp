class Solution:
    def intervalIntersection(self, A, B):
        i = j = 0
        ans = []

        while i < len(A) and j < len(B):
            start = max(A[i][0], B[j][0])
            end = min(A[i][1], B[j][1])

            if start <= end:
                ans.append([start, end])

            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1

        return ans
