from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        # Deques to keep track of indices of the max and min values in the current window
        max_deque = deque()
        min_deque = deque()
        
        left = 0  # Left pointer of the sliding window
        result = 0  # Variable to store the length of the longest valid subarray
        
        # Iterate over the array with the right pointer
        for right in range(len(nums)):
            # Maintain the max deque: remove elements from the back while they are <= current element
            while max_deque and nums[max_deque[-1]] <= nums[right]:
                max_deque.pop()
            max_deque.append(right)
            
            # Maintain the min deque: remove elements from the back while they are >= current element
            while min_deque and nums[min_deque[-1]] >= nums[right]:
                min_deque.pop()
            min_deque.append(right)
            
            # Ensure the window is valid: the difference between the max and min values is within the limit
            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                left += 1  # Move the left pointer to the right to shrink the window
                # Remove the leftmost element from the max deque if it's outside the window
                if max_deque[0] < left:
                    max_deque.popleft()
                # Remove the leftmost element from the min deque if it's outside the window
                if min_deque[0] < left:
                    min_deque.popleft()
                    
            # Update the result with the length of the current valid window
            result = max(result, right - left + 1)
        
        return result
