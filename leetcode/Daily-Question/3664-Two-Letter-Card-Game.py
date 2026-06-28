class Solution:
    def score(self, cards: List[str], x: str) -> int:
        ans = 0

        for card in cards:
            if card[0] == x:
                ans += 1
            if card[1] == x:
                ans += 1

        return ans
