# LC 54. Spiral Matrix | Medium
class Solution:
    def spiralOrder(self, matrix):
        if not matrix: return []
        res = []
        top, bot, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1
        while top <= bot and left <= right:
            for i in range(left, right+1): res.append(matrix[top][i])
            top += 1
            for i in range(top, bot+1): res.append(matrix[i][right])
            right -= 1
            if top <= bot:
                for i in range(right, left-1, -1): res.append(matrix[bot][i])
                bot -= 1
            if left <= right:
                for i in range(bot, top-1, -1): res.append(matrix[i][left])
                left += 1
        return res
