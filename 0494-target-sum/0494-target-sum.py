class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        # Memoization Solution

        memo = {}

        def helper(i, current_sum):
            # Check if the result is already computed
            if (i, current_sum) in memo:
                return memo[(i, current_sum)]

            # base case: when all members are processed
            if i == len(nums):
                return 1 if current_sum == target else 0

            # Recursive case: compute the number of ways by adding or subtracting 
            add = helper(i + 1, current_sum + nums[i])
            subtract = helper(i + 1, current_sum - nums[i])


            memo[(i, current_sum)] = add + subtract

            return memo[(i, current_sum)]

        return helper(0, 0)
        
        
        
        
        
        
        
        
        
        
        
        
        # # Recursive solution
        # def helper(i, current_sum):
        #     # Base case: if we have processed all numbers, check if sum is equal to target
        #     if i == len(nums):
        #         return 1 if current_sum == target else 0

        #     # Recursion for both adding and subtracting the current number
        #     add = helper(i + 1, current_sum + nums[i])

        #     subtract = helper( i + 1, current_sum - nums[i])

        #     return add + subtract

        # return helper(0,0)















