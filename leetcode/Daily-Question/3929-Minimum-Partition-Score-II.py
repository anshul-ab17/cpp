class Solution:
    def minPartitionScoreII(self, nums: list[int], k: int) -> int:
        n = len(nums)

        def valid(limit):
            cnt = 1
            cur_min = nums[0]
            cur_max = nums[0]

            for i in range(1, n):
                nxt_min = min(cur_min, nums[i])
                nxt_max = max(cur_max, nums[i])

                if nxt_max - nxt_min <= limit:
                    cur_min = nxt_min
                    cur_max = nxt_max
                else:
                    cnt += 1
                    cur_min = cur_max = nums[i]

                    if cnt > k:
                        return False

            return True

        low = 0
        high = max(nums) - min(nums)
        ans = high

        while low <= high:
            mid = (low + high) // 2

            if valid(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
