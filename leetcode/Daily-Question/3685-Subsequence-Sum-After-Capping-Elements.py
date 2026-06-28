def subsequenceSumAfterCapping(nums: list[int], cap: int) -> int:
    # Transform elements according to capping rule
    capped_nums = [min(x, cap) for x in nums]
    
    # Depending on the exact constraint (e.g., sum of all subsequences or max subsequence):
    # Here is the sum of all non-empty subsequence sums:
    total_sum = 0
    n = len(capped_nums)
    MOD = 10**9 + 7
    
    for x in capped_nums:
        # Each element contributes to 2^(n-1) subsequences
        total_sum = (total_sum + x * pow(2, n - 1, MOD)) % MOD
        
    return total_sum
