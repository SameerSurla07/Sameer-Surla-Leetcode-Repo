class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        
        
        # Optimal Approach

        # Function to calculate the sum of all subarray maximums
        def calculate_sum_of_maximums(nums: List[int]) -> int:
            n = len(nums)
            # Stack to store indices of elements
            stack = []
            sum_max = 0
            
            for i in range(n):
                # Maintain elements in the stack such that they are in decreasing order
                while stack and nums[stack[-1]] <= nums[i]:
                    index = stack.pop()
                    # Calculate the contribution of nums[index] as maximum in subarrays
                    left = stack[-1] if stack else -1
                    right = i
                    sum_max += nums[index] * (index - left) * (right - index)
                stack.append(i)
                
            # Process remaining elements in the stack
            while stack:
                index = stack.pop()
                left = stack[-1] if stack else -1
                right = n
                sum_max += nums[index] * (index - left) * (right - index)
            
            return sum_max
        
        # Function to calculate the sum of all subarray minimums
        def calculate_sum_of_minimums(nums: List[int]) -> int:
            n = len(nums)
            stack = []
            sum_min = 0
            
            for i in range(n):
                # Maintain elements in the stack such that they are in increasing order
                while stack and nums[stack[-1]] >= nums[i]:
                    index = stack.pop()
                    # Calculate the contribution of nums[index] as minimum in subarrays
                    left = stack[-1] if stack else -1
                    right = i
                    sum_min += nums[index] * (index - left) * (right - index)
                stack.append(i)
            
            # Process remaining elements in the stack
            while stack:
                index = stack.pop()
                left = stack[-1] if stack else -1
                right = n
                sum_min += nums[index] * (index - left) * (right - index)
            
            return sum_min
        
        # Calculate the sum of all subarray maximums and minimums
        sum_max = calculate_sum_of_maximums(nums)
        sum_min = calculate_sum_of_minimums(nums)
        
        # The result is the difference between the two
        return sum_max - sum_min


        
        # # Brute Force Approach
        
        # n = len(nums)
        # total_sum = 0
        
        # # Iterate through all possible starting points of subarrays
        # for i in range(n):
        #     min_val = nums[i]
        #     max_val = nums[i]
            
        #     # Extend the subarray to include elements up to index j
        #     for j in range(i, n):
        #         # Update the minimum value in the current subarray
        #         min_val = min(min_val, nums[j])
        #         # Update the maximum value in the current subarray
        #         max_val = max(max_val, nums[j])
                
        #         # Calculate the range (max - min) for the current subarray
        #         # and add it to the total sum
        #         total_sum += max_val - min_val
        
        # return total_sum
