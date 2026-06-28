class Solution:
    def countEffectiveSubsequences(self, nums: list[int]) -> int:
        MOD = 10**9 + 7

        total_or = 0
        for num in nums:
            total_or |= num

        if total_or == 0:
            return 0

        active_bits = [b for b in range(21) if total_or & (1 << b)]
        k = len(active_bits)

        ans = 0

        for mask in range(1, 1 << k):
            bits_mask = 0
            bits_count = 0

            for i in range(k):
                if mask & (1 << i):
                    bits_mask |= (1 << active_bits[i])
                    bits_count += 1

            invalid_count = 0
            for num in nums:
                if (num & bits_mask) == 0:
                    invalid_count += 1

            ways = pow(2, invalid_count, MOD)

            if bits_count & 1:
                ans = (ans + ways) % MOD
            else:
                ans = (ans - ways + MOD) % MOD

        return ans
