from collections import Counter

class Solution:
    def smallestPermutation(self, s: str, target: str) -> str:
        n = len(s)
        total_counts = Counter(s)
        prefix_counts = Counter()

        best_index = -1
        best_char = None

        for i in range(n):
            for c_code in range(ord(target[i]) + 1, ord('z') + 1):
                c = chr(c_code)
                if total_counts[c] - prefix_counts[c] > 0:
                    best_index = i
                    best_char = c

            if total_counts[target[i]] - prefix_counts[target[i]] > 0:
                prefix_counts[target[i]] += 1
            else:
                break

        if best_index == -1:
            return ""

        ans_chars = []
        rem_counts = Counter(s)

        for i in range(best_index):
            ans_chars.append(target[i])
            rem_counts[target[i]] -= 1

        ans_chars.append(best_char)
        rem_counts[best_char] -= 1

        for c in sorted(rem_counts.keys()):
            if rem_counts[c] > 0:
                ans_chars.extend([c] * rem_counts[c])

        return "".join(ans_chars)
