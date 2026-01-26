class Solution:
    def minAvailableDuration(self, s1, s2, duration):
        s1.sort(); s2.sort()
        i = j = 0

        while i < len(s1) and j < len(s2):
            start = max(s1[i][0], s2[j][0])
            end = min(s1[i][1], s2[j][1])

            if end - start >= duration:
                return [start, start + duration]

            if s1[i][1] < s2[j][1]:
                i += 1
            else:
                j += 1

        return []
