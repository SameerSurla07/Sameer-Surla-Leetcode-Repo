#User function Template for python3

from typing import List
class Solution:
    def numOfIslands(self, rows: int, cols : int, operators : List[List[int]]) -> List[int]:
        # code here
        
        # Helper function to find the root of a given cell using path compression
        def find(parent, x):
            if parent[x] != x:
                parent[x] = find(parent, parent[x])   # Path compression
            return parent[x]
        
        # Helper function to unite two sets
        def union(parent, rank, x, y):
            rootX = find(parent, x)
            rootY = find(parent, y)
            if rootX != rootY: # Only union if they are in different sets
                if rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    parent[rootX] = rootY
                else:
                    parent[rootY] = rootX
                    rank[rootX] += 1
                
        # Directions for moving up, down, left, right
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        
        # Step 1: Initialize the result array, parent array,
        # rank array, and set for visited land cells
        result = []
        parent = {}
        rank = {}
        island_count = 0
        visited = set()
        
        # Step 2: Process each operator ( each land placement )
        for op in operators:
            x,y = op
            cell_id = (x,y)  # We can use a tuple as a unique identifier for each cell
            
            if cell_id in visited:
                result.append(island_count)
                continue
            
            # Mark the cell as visited and initialize its parent
            # and rank 
            visited.add(cell_id)
            parent[cell_id] = cell_id
            rank[cell_id] = 0
            island_count += 1
            
            # Step 3: check for all directions 
            for d in directions:
                nx, ny = x + d[0], y + d[1]
                neighbor_id = (nx, ny)
                
                if 0 <= nx < n and 0 <= ny < m and neighbor_id in visited:
                    # If the neighbor is within bounds and is a land cell, try to union them
                    if find(parent, cell_id) != find(parent, neighbor_id):
                        union(parent, rank, cell_id, neighbor_id)
                        island_count -= 1
                        
            # Append the current number of islands after processing this operation
            result.append(island_count)

        return result
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3


    
if __name__=="__main__":
    T = int(input())
    for t in range(T):
        
        n = int(input())
        m = int(input())
        k = int(input())
        operators = []
        for i in range(k):
            u, v = map(int, input().strip().split())
            operators.append([u, v])
        obj = Solution()
        ans = obj.numOfIslands(n, m, operators)
        for i in ans:
            print(i, end = ' ')
        print()
            

# } Driver Code Ends