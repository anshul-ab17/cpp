class Solution:
    def minGenerations(self, start: list[int], target: list[int]) -> int:
        sx, sy = start
        tx, ty = target

        ans = 0

        while tx >= sx and ty >= sy:
            if tx == sx and ty == sy:
                return ans

            if tx > ty:
                if ty == sy:
                    return (
                        ans + (tx - sx) // ty
                        if (tx - sx) % ty == 0
                        else -1
                    )

                steps = tx // ty
                ans += steps
                tx %= ty

            elif ty > tx:
                if tx == sx:
                    return (
                        ans + (ty - sy) // tx
                        if (ty - sy) % tx == 0
                        else -1
                    )

                steps = ty // tx
                ans += steps
                ty %= tx

            else:
                return -1

        return -1
