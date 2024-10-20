class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Function to perform DFS and mark all connected '1's as visited
        def dfs(x: int, y: int):
            # Base case: check boundaries and if the cell is water or already visited
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == '0':
                return
            # Mark the current cell as visited
            grid[x][y] = '0'
            # Explore all four directions
            dfs(x + 1, y)  # Down
            dfs(x - 1, y)  # Up
            dfs(x, y + 1)  # Right
            dfs(x, y - 1)  # Left
        
        if not grid:
            return 0
        
        m, n = len(grid), len(grid[0])
        island_count = 0
        
        # Iterate through each cell in the grid
        for i in range(m):
            for j in range(n):
                # If the cell is land, start a new DFS to mark the whole island
                if grid[i][j] == '1':
                    dfs(i, j)
                    island_count += 1
        
        return island_count