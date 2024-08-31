#User function Template for python3

import sys
from typing import List
from collections import deque
sys.setrecursionlimit(10**8)

class Solution:
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        # code here
        m = len(grid)
        n = len(grid[0])
        
        def dfs(x,y, baseX, baseY, path):
            if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                grid[x][y] = 0  # Mark the cell as visited
                # Record the relative position of this cell to the starting cell
                path.add((x - baseX, y - baseY))

                # Explore all 4 directions
                dfs(x + 1, y, baseX, baseY, path)
                dfs(x - 1, y, baseX, baseY, path)
                dfs(x, y + 1, baseX, baseY, path)
                dfs(x, y - 1, baseX, baseY, path)
                
        unique_islands = set()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:  # Found an unvisisted island part
                    path = set()
                    dfs(i, j, i, j, path)  # Perform DFS to get the island shape
                    
                    # Add the normalized shape to the set of unique islands
                    unique_islands.add(frozenset(path))
            
        return len(unique_islands)
                    























#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj=Solution()
        print(obj.countDistinctIslands(grid))
# } Driver Code Ends