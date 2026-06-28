class Solution:
    def minOperations(self, nums: list[int], k: int, queries: list[list[int]]) -> list[int]:
        n = len(nums)

        rem = [x % k for x in nums]

        diff_prefix = [0] * n
        for i in range(1, n):
            diff_prefix[i] = diff_prefix[i - 1]
            if rem[i] != rem[i - 1]:
                diff_prefix[i] += 1

        ans = []

        for l, r in queries:
            if l == r:
                ans.append(0)
                continue

            if diff_prefix[r] - diff_prefix[l] > 0:
                ans.append(-1)
                continue

            sub = sorted(nums[i] // k for i in range(l, r + 1))
            median = sub[len(sub) // 2]

            ops = sum(abs(x - median) for x in sub)
            ans.append(ops)

        return ans
