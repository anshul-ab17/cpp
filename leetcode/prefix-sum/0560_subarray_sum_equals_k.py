# LC 560. Subarray Sum Equals K | Medium
class Solution:
    def subarraySum_brute(self, nums, k):
        count = 0
        for i in range(len(nums)):
            s = 0
            for j in range(i, len(nums)):
                s += nums[j]
                if s == k: count += 1
        return count

    # Prefix sum + hashmap - O(n)
    def subarraySum(self, nums, k):
        count, cur = 0, 0
        prefix = {0: 1}
        for num in nums:
            cur += num
            count += prefix.get(cur - k, 0)
            prefix[cur] = prefix.get(cur, 0) + 1
        return count
