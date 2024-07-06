from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        pre, suff = 1, 1
        ans = float('-inf')
        for i in range(n):
            if pre == 0:
                pre = 1
            if suff == 0:
                suff = 1
            pre *= nums[i]
            suff *= nums[n - i - 1]
            ans = max(ans, max(pre, suff))
        return ans    
        
        # n = len(nums)
        # result = nums[0]
        
        # for i in range(n):
        #     prod = 1  # Initialize product to 1
        #     for j in range(i, n):  # Start from i to n (inclusive of i)
        #         prod *= nums[j]
        #         result = max(result, prod)  # Update result with max product
                
        # return result