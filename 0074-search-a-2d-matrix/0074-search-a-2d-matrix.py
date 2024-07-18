class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # Better Approach

        def binarysearch ( nums, target):
            n = len(nums)
            low = 0
            high = n - 1

            while low <= high :
                mid = ( low + high ) // 2

                if nums[mid] == target:
                    return True
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            return False

        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):
            if matrix[i][0] <= target <= matrix[i][m-1]:
                return binarysearch(matrix[i], target)
        return False

    



        # Brute Force Approach

        # m = len(matrix)
        # n = len(matrix[0])

        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == target:
        #             return True
        # return False