def maxAlternatingSum(nums: list[int], max_swaps: int) -> int:
    # Separate elements into positive positions (even indices) and negative positions (odd indices)
    n = len(nums)
    even_indices = sorted([nums[i] for i in range(0, n, 2)])
    odd_indices = sorted([nums[i] for i in range(1, n, 2)], reverse=True)
    
    # We want large numbers in even positions, small numbers in odd positions
    swaps_done = 0
    i, j = 0, 0
    
    while swaps_done < max_swaps and i < len(even_indices) and j < len(odd_indices):
        if even_indices[i] < odd_indices[j]:
            # Swap them
            even_indices[i], odd_indices[j] = odd_indices[j], even_indices[i]
            swaps_done += 1
            i += 1
            j += 1
        else:
            break
            
    return sum(even_indices) - sum(odd_indices)
