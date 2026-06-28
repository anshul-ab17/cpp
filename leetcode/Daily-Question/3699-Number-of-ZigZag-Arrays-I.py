
def countZigZagArrays(nums: list[int]) -> int:
    n = len(nums)
    if n < 2:
        return n
        
    # up[i] = length of zigzag ending at i with an upward slope
    # down[i] = length of zigzag ending at i with a downward slope
    up = [1] * n
    down = [1] * n
    total_zigzag_subarrays = n  # Every single element is a valid zigzag of length 1
    
    for i in range(1, n):
        if nums[i] > nums[i-1]:
            up[i] = down[i-1] + 1
            total_zigzag_subarrays += (up[i] - 1)
        elif nums[i] < nums[i-1]:
            down[i] = up[i-1] + 1
            total_zigzag_subarrays += (down[i] - 1)
            
    return total_zigzag_subarrays
