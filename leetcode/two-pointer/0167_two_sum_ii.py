# LC 167. Two Sum II - Input Array Is Sorted | Medium
class Solution:
    def twoSum_brute(self, numbers, target):
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]

    # Two pointers - O(n)
    def twoSum(self, numbers, target):
        l, r = 0, len(numbers) - 1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target: return [l + 1, r + 1]
            elif s < target: l += 1
            else: r -= 1
