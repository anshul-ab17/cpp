class Solution:
    def bowlSubarrays(self, nums: list[int]) -> int:
        result = 0
        stack = []
        
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
                if stack:
                    result += 1
            stack.append(i)
            
        return result
