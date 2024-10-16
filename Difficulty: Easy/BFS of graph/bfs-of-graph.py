from collections import deque
from typing import List

#User function Template for python3
class Solution:
    # Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, adj: List[List[int]]) -> List[int]:
        #code here
        visited = [False] * len(adj)
        
        result = []
        
        queue = deque([0])
        
        visited[0] = True
        
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            
            # Visit all neighbors in the order they appear
            for neighbor in adj[vertex]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True
                    
        return result
        
        
        
        
        
        
        
        
        
        
        











#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        V, E = map(int, input().split())
        adj = [[] for i in range(V)]
        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)  # This line ensures the graph is undirected
        ob = Solution()
        ans = ob.bfsOfGraph(adj)
        for i in range(len(ans)):
            print(ans[i], end=" ")
        print()

# } Driver Code Ends