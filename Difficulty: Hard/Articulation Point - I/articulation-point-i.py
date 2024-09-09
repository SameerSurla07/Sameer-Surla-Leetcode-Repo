#User function Template for python3

import sys
sys.setrecursionlimit(10**6)

class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    def articulationPoints(self, V, adj):
        # code here

        # Helper function to perfrom DFS and find articulation points
        def dfs(u, parent, visited, discovery, low, ap, time):
            
            # Mark the current node as visited
            visited[u] = True
            # Initialize discovery time and low-link value
            discovery[u] = low[u] = time
            time += 1
            children = 0  # track the number of children in DFS
            
            # Traverse all adjacent vertices
            for v in adj[u]:
                if not visited[v]:
                    children += 1
                    dfs(v, u, visited, discovery, low, ap, time)
            
                    # Check if the subtree rooted at v has a back edge to an ancestor of u
                    low[u] = min(low[u], low[v])
                    
                    # Articulation point condition for non-root nodes
                    if parent != -1 and low[v] >= discovery[u]:
                        ap[u] = True
                        
                elif v != parent:
                    # Update low[u] for back edges
                    low[u] = min(low[u], discovery[v])
                    
            # Root node is an articulation point is it has more than one child
            if parent == -1 and children > 1:
                ap[u] = True
                
        # Initialize arrays
        visited = [False] * V
        discovery = [-1] * V
        low = [-1] * V
        ap = [False] * V
        time = 0
        
        # Run DFS for each unvisited node
        for i in range(V):
            if not visited[i]:
                dfs(i, -1 , visited, discovery, low, ap , time)
                
        # Colelct and return articulation point in sorted order
        result = [i for i in range(V) if ap[i]]
        return result if result else [-1]















#{ 
 # Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		ob = Solution()
		ans = ob.articulationPoints(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends