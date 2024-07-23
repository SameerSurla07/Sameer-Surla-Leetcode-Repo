class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Initialize the result list with -1 for all elements
        result = [-1] * n
        stack = []

        # Loop through the array twice to handle the circular nature
        for i in range(2 * n):
            # Use modulo to get the index in the original array
            while stack and nums[stack[-1]] < nums[i % n]:
                result[stack.pop()] = nums[i % n]
            
            if i < n:
                stack.append(i)
        
        return result
