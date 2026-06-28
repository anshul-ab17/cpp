from collections import Counter

class Solution:
    def smallestPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        counts = Counter(s)

        odd_chars = [c for c, qty in counts.items() if qty % 2 != 0]
        if len(odd_chars) > 1:
            return ""

        center_char = odd_chars[0] if odd_chars else ""

        half_pool = Counter()
        for c, qty in counts.items():
            half_pool[c] = qty // 2

        half_len = n // 2
        best_idx = -1
        best_char = None

        prefix_half = Counter()

        for i in range(half_len):
            for c_code in range(ord(target[i]) + 1, ord('z') + 1):
                c = chr(c_code)
                if half_pool[c] - prefix_half[c] > 0:
                    best_idx = i
                    best_char = c

            if half_pool[target[i]] - prefix_half[target[i]] > 0:
                prefix_half[target[i]] += 1
            else:
                break

        if best_idx == -1 and n % 2 == 1:
            if center_char > target[half_len]:
                best_idx = half_len
                best_char = center_char

        if best_idx == -1:
            return ""

        res_half = []
        rem_half = Counter(half_pool)

        for i in range(min(best_idx, half_len)):
            res_half.append(target[i])
            rem_half[target[i]] -= 1

        if best_idx < half_len:
            res_half.append(best_char)
            rem_half[best_char] -= 1

            for c in sorted(rem_half.keys()):
                if rem_half[c] > 0:
                    res_half.extend([c] * rem_half[c])

            first_half = "".join(res_half)
            full_str = first_half + center_char + first_half[::-1]
        else:
            first_half = target[:half_len]
            full_str = first_half + best_char + first_half[::-1]

        return full_str if full_str > target else ""
