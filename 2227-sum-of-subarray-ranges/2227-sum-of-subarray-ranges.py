class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = 0
        
        # Iterate through all possible starting points of subarrays
        for i in range(n):
            min_val = nums[i]
            max_val = nums[i]
            
            # Extend the subarray to include elements up to index j
            for j in range(i, n):
                # Update the minimum value in the current subarray
                min_val = min(min_val, nums[j])
                # Update the maximum value in the current subarray
                max_val = max(max_val, nums[j])
                
                # Calculate the range (max - min) for the current subarray
                # and add it to the total sum
                total_sum += max_val - min_val
        
        return total_sum
