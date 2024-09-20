class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        # Approach 3: Tabulation Method ( bottom-up DP)

        # TC - 
        # SC - 

        # We use a DP, where dp[j] tells whether can form a
        # subset sum j

        # initilization dp[0] = True since a sum of 0 can be
        # always formed

        # FOr each number in the array, we update the table
        # from right to left to avoid overwriting the results
        # of the current number

        total_sum = sum(nums)

        # Base case: if total_sum is odd, equal partition = False
        if total_sum % 2 != 0:
            return False

        target = total_sum // 2
        
        # Initialize DP table with False values of length target + 1
        dp = [False] * ( target + 1 )
        dp[0] = True  # We can always make sum 0 by taking no elements

        # Iterate over each number
        for num in nums:
            # Traverse the dp array from right to left
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        # Final result will be if we can form sum target
        return dp[target]
        
        
        
        
        
        
        
        
        
        
        
        
        # Approach 2: Memoized Recursion ( Top -down DP )

        # TC - O( n * target)
        # SC - O(n * target) for memo table and recursion stack

        total_sum = sum(nums)

        # Base case: If sum of nums is odd, no possible partition
        if total_sum % 2 != 0:
            return False

        target = total_sum // 2

        memo = {}

        def subsetSum(index, current_sum, memo):
            # If sum is already achieved, return True
            if current_sum == 0:
                return True

            # If no more items to process or the sum becomes negative
            if index == 0 or current_sum < 0:
                return False

            # Check if result is already computed
            if (index, current_sum) in memo:
                return memo[(index, current_sum)]

            # Option 1: Exclude the current element
            exclude = subsetSum(index - 1, current_sum, memo)

            # Option 2: Include the current element
            include = subsetSum(index - 1, current_sum - nums[index - 1], memo)
        
            memo[(index, current_sum)] = exclude or include

            return memo[(index, current_sum)]

        return subsetSum(len(nums) -1, target, memo)       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # # Approach 1: Basic recursion

        # TC - O(2^n) - checking all possible subsets
        # SC - O(n) for recursion stack 

        # total_sum = sum(nums)

        # # If total sum is odd, return False
        # if total_sum % 2 != 0:
        #     return False

        # target = total_sum // 2
        
        # def subsetSum(index, current_sum):
        #     # Base case: when target sum is achieved
        #     if current_sum == 0:
        #         return True
            
        #     # If no more items to process or the sum becomes negative
        #     if index == 0 or current_sum < 0:
        #         return False

        #     # Option 1: Exclude the current element and check the rest
        #     exclude = subsetSum(index - 1, current_sum)

        #     # Option 2: Include the current element and check the remaninig
        #     include = subsetSum(index - 1, current_sum - nums[index - 1])

        #     return exclude or include

        # return subsetSum(len(nums), target)  # (index, target)


