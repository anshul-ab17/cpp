# Floyd Cycle Detection on circular array.
class Solution:
    def circularArrayLoop(self, nums):
        n = len(nums)

        def next_idx(i):
            return (i + nums[i]) % n

        for i in range(n):
            if nums[i] == 0:
                continue

            slow, fast = i, i
            while True:
                if nums[slow] * nums[next_idx(slow)] <= 0:
                    break
                if nums[fast] * nums[next_idx(fast)] <= 0:
                    break
                nxt_fast = next_idx(fast)
                if nums[fast] * nums[next_idx(nxt_fast)] <= 0:
                    break
                slow = next_idx(slow)
                fast = next_idx(next_idx(fast))
                if slow == fast:
                    if slow == next_idx(slow):
                        break
                    return True

            j = i
            val = nums[i]
            while nums[j] * val > 0:
                nxt = next_idx(j)
                nums[j] = 0
                j = nxt

        return False
