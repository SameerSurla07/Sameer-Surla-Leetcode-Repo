class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        # Binary Search
        n = len(nums)

        low = 0
        high = n-1
        if target <= nums[0]:
            return 0

        if target > nums[n-1]:
            return n

        while low <= high :
            mid  = ( low + high ) // 2
            if nums[mid] == target :
                return mid
            elif nums[mid] > target : 
                high = mid - 1
            else:
                low = mid + 1

        return low

        #  Basic linear search O(N)
        # n = len(nums)
        # mini = n-1
        # if target > nums[n-1]:
        #     mini = n

        # if target < nums[0]:
        #     mini = 0

        # for i in range(n):
        #     if nums[i] >= target:
        #         mini = i
        #         break

        # return mini

            
