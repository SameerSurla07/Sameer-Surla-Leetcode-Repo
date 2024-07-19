class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:

        def find_max_in_col(col):
            max_row = 0
            for i in range(len(mat)):
                if mat[i][col] > mat[max_row][col]:
                    max_row = i
            return max_row

        def find_max_in_row(row):
            max_col = 0
            for j in range(len(mat[0])):
                if mat[row][j] > mat[row][max_col]:
                    max_col = j
            return max_col
        
        m, n = len(mat), len(mat[0])
        left, right = 0, n - 1

        while left <= right:
            mid_col = (left + right) // 2
            max_row = find_max_in_col(mid_col)
            
            if (mid_col == 0 or mat[max_row][mid_col] > mat[max_row][mid_col - 1]) and \
            (mid_col == n - 1 or mat[max_row][mid_col] > mat[max_row][mid_col + 1]):
                return [max_row, mid_col]
            elif mid_col > 0 and mat[max_row][mid_col - 1] > mat[max_row][mid_col]:
                right = mid_col - 1
            else:
                left = mid_col + 1