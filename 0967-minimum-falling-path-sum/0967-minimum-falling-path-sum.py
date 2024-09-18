class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        # Tabulation

        m, n = len(matrix) , len(matrix[0])

        dp = [[0] * n for _ in range(m)]

        # Initialize the last row witht the values from the matrix
        for j in range(n):
            dp[m-1][j] = matrix[m-1][j]

        # build the dp table from the second last row upwards
        for i in range(m-2, -1, -1):
            for j in range(n):
                down = dp[i+1][j]
                left_diagonal = dp[i+1][j-1] if j-1 >= 0 else float('inf')
                right_diagonal = dp[i+1][j+1] if j+1 < n  else float('inf')
                dp[i][j] = matrix[i][j] + min(down, left_diagonal, right_diagonal)

        return min(dp[0])


        







        
        # # Memoization Solution

        # m, n = len(matrix), len(matrix[0])

        # dp = [ [-1] * n for _ in range(m)]

        # def recurse(i, j):
        #     if j < 0 or j >= n:  # Out of bounds
        #         return float('inf') 
        #     if i == m - 1:  # Base case : last row
        #         return matrix[i][j]

        #     if dp[i][j] != -1:  # If already computed
        #         return dp[i][j]

        #     # Recursively calculate the minimum path sum
        #     down = recurse(i + 1, j)
        #     left_diagonal = recurse(i + 1, j - 1)
        #     right_diagonal = recurse(i + 1, j + 1)

        #     dp[i][j] = matrix[i][j] + min(down, left_diagonal, right_diagonal)
        #     return dp[i][j]

        # min_sum = float('inf')
        # for j in range(n):
        #     min_sum = min( min_sum, recurse(0, j))
        # return min_sum