class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, index: int, val: int) -> None:
        while index <= self.n:
            self.tree[index] = max(self.tree[index], val)
            index += index & (-index)  # å¾åæ´æ°

    def preSum(self, pos):
        # æç§é¢æçæ¹å¼æ±åç¼æå¤§å¼
        ans = 0
        while pos >= 1:
            ans = max(ans, self.tree[pos])
            pos -= pos & (-pos)
        return ans


class Solution:
    def maxAlternatingSum(self, nums: list[int], k: int) -> int:
        stl = sorted(set(nums))  # å°numsä¸­ä¸åçæ°å­è¿è¡æåº
        rank = {
            v: i + 1 for i, v in enumerate(stl)
        }  # å°numsä¸­çå¼å¿«éè½¬æ¢æstlä¸­çç´¢å¼
        fwt0 = FenwickTree(len(stl))
        fwt1 = FenwickTree(len(stl))

        n = len(nums)
        dp = [[0, 0] for _ in range(n)]
        res = nums[0]
        for i in range(n):
            dp[i][0] = dp[i][1] = nums[i]
            if i >= k:
                indx = rank[nums[i]]  # æ¾å°nums[i]å¨stlä¸­çç´¢å¼
                dp[i][1] = max(
                    dp[i][1], fwt0.preSum(indx - 1) + nums[i]
                )  # indx-1å³è¡¨ç¤ºå°äºnums[i]çé¨å
                dp[i][0] = max(
                    dp[i][0], fwt1.preSum(len(stl) - indx) + nums[i]
                )  # len(stl)-indxå³è¡¨ç¤ºå¨ååºåè¡¨ä¸­å¤§äºnums[i]çé¨å

            if i - k + 1 >= 0:
                indx = rank[nums[i - k + 1]]
                fwt0.update(indx, dp[i - k + 1][0])  # å¨æ­£åºåè¡¨ä¸­æ´æ°i-k+1ä½ç½®çå¼
                fwt1.update(
                    len(stl) - indx + 1, dp[i - k + 1][1]
                )  # å¨ååºåè¡¨ä¸­æ´æ°i-k+1ä½ç½®çå¼

            res = max(res, dp[i][0], dp[i][1])  # æ´æ°ç­æ¡

        return res
