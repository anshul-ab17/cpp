def maxXORSubsequence(nums: list[int]) -> int:
    # Linear Basis (Gaussian Elimination in GF(2)) to find max XOR
    basis = []
    for num in nums:
        for b in basis:
            num = min(num, num ^ b)
        if num > 0:
            basis.append(num)
            basis.sort(reverse=True)
            
    res = 0
    for b in basis:
        res = max(res, res ^ b)
    return res
