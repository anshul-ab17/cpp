class Solution:
    def totalScore(self, hp: int, damage: list[int], requirement: list[int]) -> int:
        n = len(damage)

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + damage[i]

        total = 0

        for i in range(n):
            if hp - damage[i] < requirement[i]:
                continue

            limit = hp - damage[i] - requirement[i]

            low, high = 0, i
            earliest = i

            while low <= high:
                mid = (low + high) // 2

                if prefix[i] - prefix[mid] <= limit:
                    earliest = mid
                    high = mid - 1
                else:
                    low = mid + 1

            total += i - earliest + 1

        return total
