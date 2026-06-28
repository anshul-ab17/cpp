class Solution:
    def maxCyclicPartitionScore(self, nums: list[int], k: int) -> int:
        n = len(nums)

        if k >= n:
            k = n

        extended_nums = nums + nums
        max_score = 0

        for start_idx in range(min(n, 50)):
            arr = extended_nums[start_idx:start_idx + n]

            dp = [[-1] * (k + 1) for _ in range(n + 1)]
            dp[0][0] = 0

            for j in range(1, k + 1):
                for i in range(1, n + 1):
                    curr_max = -float('inf')
                    curr_min = float('inf')

                    for p in range(i - 1, -1, -1):
                        if dp[p][j - 1] != -1:
                            if arr[p] > curr_max:
                                curr_max = arr[p]

                            if arr[p] < curr_min:
                                curr_min = arr[p]

                            score = dp[p][j - 1] + (curr_max - curr_min)

                            if score > dp[i][j]:
                                dp[i][j] = score

            for j in range(1, k + 1):
                max_score = max(max_score, dp[n][j])

        return max_score
