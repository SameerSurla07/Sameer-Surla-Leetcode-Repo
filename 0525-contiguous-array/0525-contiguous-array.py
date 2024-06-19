class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # HashMap to store the first occurrence of each prefix sum
        prefix_sum_indices = {}
        # Initialize max_length to store the maximum length of the subarray
        max_length = 0
        # Initialize current_sum to store the prefix sum
        current_sum = 0
        
        for i in range(len(nums)):
            # Convert 0 to -1
            if nums[i] == 0:
                current_sum -= 1
            else:
                current_sum += 1
            
            # Check if the current sum is zero
            if current_sum == 0:
                max_length = max(max_length, i + 1)
            else:
                # If current sum has been seen before
                if current_sum in prefix_sum_indices:
                    # Update max_length with the length of the subarray
                    max_length = max(max_length, i - prefix_sum_indices[current_sum])
                else:
                    # Store the first occurrence of the current sum
                    prefix_sum_indices[current_sum] = i
        
        return max_length
