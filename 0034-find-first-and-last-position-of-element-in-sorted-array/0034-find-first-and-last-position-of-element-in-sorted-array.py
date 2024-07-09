class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findFirst(nums: List[int], target: int) -> int:
            low, high = 0, len(nums) - 1
            first_pos = -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] < target:
                    low = mid + 1
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    first_pos = mid
                    high = mid - 1  # Continue searching in the left half
            return first_pos
        
        def findLast(nums: List[int], target: int) -> int:
            low, high = 0, len(nums) - 1
            last_pos = -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] < target:
                    low = mid + 1
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    last_pos = mid
                    low = mid + 1  # Continue searching in the right half
            return last_pos

        first_pos = findFirst(nums, target)
        if first_pos == -1:
            return [-1, -1]
        
        last_pos = findLast(nums, target)
        
        return [first_pos, last_pos]