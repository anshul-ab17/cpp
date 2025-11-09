# LC 4. Median of Two Sorted Arrays | Hard | Google
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        A, B = nums1, nums2
        if len(A) > len(B): A, B = B, A
        m, n = len(A), len(B)
        lo, hi = 0, m
        while lo <= hi:
            i = (lo + hi) // 2
            j = (m + n + 1) // 2 - i
            left_a = A[i-1] if i > 0 else float('-inf')
            right_a = A[i] if i < m else float('inf')
            left_b = B[j-1] if j > 0 else float('-inf')
            right_b = B[j] if j < n else float('inf')
            if left_a <= right_b and left_b <= right_a:
                if (m + n) % 2: return max(left_a, left_b)
                return (max(left_a, left_b) + min(right_a, right_b)) / 2
            elif left_a > right_b: hi = i - 1
            else: lo = i + 1
