import math

class Solution:
    def minimumTime(self, d: list[int], r: list[int]) -> int:
        lcm_val = (r[0] * r[1]) // math.gcd(r[0], r[1])

        low = 0
        high = 10**18
        ans = high

        while low <= high:
            mid = (low + high) // 2

            slots_1 = mid - (mid // r[0])
            slots_2 = mid - (mid // r[1])
            tot_slots = mid - (mid // lcm_val)

            if (
                slots_1 >= d[0]
                and slots_2 >= d[1]
                and tot_slots >= d[0] + d[1]
            ):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
