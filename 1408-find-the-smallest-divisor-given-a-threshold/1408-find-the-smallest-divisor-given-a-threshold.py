
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        # Optimal Approach

        import math
        
        def calculate_sum_divisions(divisor):
            return sum(math.ceil(num / divisor) for num in nums)
        
        left, right = 1, max(nums)
        result = max(nums)  # Initialize result to maximum possible value
        
        while left <= right:
            mid = (left + right) // 2
            sum_divisions = calculate_sum_divisions(mid)
            
            if sum_divisions <= threshold:
                result = mid  # Update result to current mid if it satisfies the condition
                right = mid - 1  # Search for potentially smaller divisor
            else:
                left = mid + 1  # Search for larger divisor
        
        return result

        # Brute Force Approach

        # import math
        
        # mindiv = float('inf')
        # max_num = max(nums)
        
        # for divisor in range(1, max_num + 1):
        #     sum_divisions = 0
        #     for num in nums:
        #         sum_divisions += math.ceil(num / divisor)
            
        #     if sum_divisions <= threshold:
        #         return divisor
        
        # return -1