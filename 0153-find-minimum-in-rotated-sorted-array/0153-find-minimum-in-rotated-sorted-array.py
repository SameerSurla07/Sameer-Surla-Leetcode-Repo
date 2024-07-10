class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        ans = 5001
        while low <= high :
            mid = ( low + high ) // 2

            if nums[low] <= nums[mid]:    
                ans = min ( ans, nums[low])
                low = mid + 1 # Eliminating left half as we got it's minimum element
            
            else:
                ans = min ( ans, nums[mid])
                high = mid - 1 # Eliminating right half as we got it's minimum element

        return ans