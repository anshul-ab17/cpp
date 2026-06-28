class Solution:
    def findMaxValue(self, n: int, diff: list[int], max_limit: list[int]) -> int:
        arr = list(max_limit)

        for i in range(1, n):
            arr[i] = min(arr[i], arr[i - 1] + diff[i - 1])

        for i in range(n - 2, -1, -1):
            arr[i] = min(arr[i], arr[i + 1] + diff[i])

        return max(arr)
