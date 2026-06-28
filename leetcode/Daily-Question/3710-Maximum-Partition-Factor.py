class Solution:
    def maxPartitionFactor(self, points: list[list[int]]) -> int:
        n = len(points)

        if n == 2:
            return 0

        dist = [[0] * n for _ in range(n)]
        max_d = 0

        for i in range(n):
            for j in range(i + 1, n):
                d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                dist[i][j] = dist[j][i] = d
                max_d = max(max_d, d)

        def isValid(mid):
            color = [-1] * n

            for i in range(n):
                if color[i] == -1:
                    queue = [i]
                    color[i] = 0
                    head = 0

                    while head < len(queue):
                        curr = queue[head]
                        head += 1

                        for neighbor in range(n):
                            if dist[curr][neighbor] < mid and curr != neighbor:
                                if color[neighbor] == -1:
                                    color[neighbor] = 1 - color[curr]
                                    queue.append(neighbor)
                                elif color[neighbor] == color[curr]:
                                    return False

            return True

        low, high = 0, max_d
        ans = 0

        while low <= high:
            mid = (low + high) // 2

            if isValid(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans
