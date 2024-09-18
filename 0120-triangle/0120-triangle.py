class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        # Memoization approach ( Recursive )
        memo = {}  # It will contain row, index as keys

        def helper(row, index):
            # Base case: If we are at last row, return the element itself
            if row == len(triangle) - 1:
                return triangle[row][index]

            # Check if result is already computed
            if (row, index) in memo:
                return memo[(row, index)]

            # Recursive case: take the minimum of the two adjacent numbers from the next row
            down = helper(row + 1, index)
            down_right = helper(row + 1, index + 1)

            # Store the result in the memo table
            memo[(row, index)] = triangle[row][index] + min(down, down_right)

            return memo[(row, index)]
        
        return helper(0,0)















