class Solution:
    def totalWaviness(self, num1: str, num2: str) -> int:
        def getWaves(num_str: str) -> int:
            if int(num_str) < 100:
                return 0

            memo = {}

            def helper(idx, isBound, twobefore, onebefore, leadingZero):
                if idx == len(num_str):
                    return (0 if leadingZero else 1, 0)

                state = (idx, isBound, twobefore, onebefore, leadingZero)
                if state in memo:
                    return memo[state]

                upper = int(num_str[idx]) if isBound else 9
                total_count = 0
                total_waves = 0

                for digit in range(upper + 1):
                    wave = 0
                    next_two = onebefore
                    next_one = digit

                    if leadingZero and digit == 0:
                        next_two = -1
                        next_one = -1
                    elif not leadingZero and twobefore != -1:
                        if (
                            (onebefore > twobefore and onebefore > digit)
                            or
                            (onebefore < twobefore and onebefore < digit)
                        ):
                            wave = 1

                    next_bound = isBound and (digit == upper)
                    next_leading = leadingZero and (digit == 0)

                    count, waves = helper(
                        idx + 1,
                        next_bound,
                        next_two,
                        next_one,
                        next_leading
                    )

                    total_count += count
                    total_waves += waves + count * wave

                memo[state] = (total_count, total_waves)
                return memo[state]

            return helper(0, True, -1, -1, True)[1]

        prev_num = str(int(num1) - 1)
        return getWaves(num2) - getWaves(prev_num)
