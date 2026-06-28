
def countStableSubsequences(nums: list[int]) -> int:
    MOD = 10**9 + 7
    n = len(nums)
    if n == 0: return 0
    
    # Dynamic programming approach tracking stable transitions
    # Example condition: stability means |nums[i] - nums[j]| <= 1
    dp = [1] * n  # Each element itself is a valid subsequence of length 1
    
    for i in range(n):
        for j in range(i):
            if abs(nums[i] - nums[j]) <= 1:
                dp[i] = (dp[i] + dp[j]) % MOD
                
    return sum(dp) % MOD
