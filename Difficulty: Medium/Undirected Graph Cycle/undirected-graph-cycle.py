from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        # Initialize the parent and rank arrays
        parent = [i for i in range(V)]  # Parent of each vertex is itself initially
        rank = [0] * V
        
        # Function to find the root of a vertex with path compression
        def find(u):
            if parent[u] != u:
                parent[u] = find(parent[u])
            return parent[u]
            
        # Function to perform union by rank
        def union(x,y):
            root_x = find(x)
            root_y = find(y)
            
            if root_x != root_y:
                if rank[root_x] > rank[root_y]:
                    parent[root_y] = root_x
                elif rank[root_y] > rank[root_x]:
                    parent[root_x] = root_y
                else:
                    parent[root_y] = root_x
                    rank[root_x] += 1
                    
        for u in range(V):
            for v in adj[u]:
                if u < v:
                    root_u = find(u)
                    root_v = find(v)
                    
                    if root_u == root_v:
                        return 1
                    else:
                        union(root_u,root_v)
                        
        return 0
                        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # Helper function to perform DFS and detect cycles
        
        # def dfs(v, parent):
        
        #     # Mark the current node as visited
        #     visited[v] = True
            
        #     # Explore all adjacent vertices of the current node
        #     for neighbor in adj[v]:
        #         # If the neighbor is not visited, continue DFS from that neighbor
        
        #         if not visited[neighbor]:
        #             if dfs(neighbor, v):/
        #                 return True  # If a cycle is detected, return True
        #         # If the neighbor is visited and is not the parent of the current node,
        #         # then we have found a back edge which indicates a cycle
        #         elif neighbor != parent:
        #             return True
            
        #     return False
    
        # Array to keep track of visited nodes
        visited = [False] * V
        
        # Iterate through each node in the graph
        for i in range(V):
            # If the node is not yet visited, perform DFS from this node
            if not visited[i]:
                if dfs(i, -1):
                    return 1  # If a cycle is detected during DFS, return 1
                    
        return 0  # If no cycle is detected, return 0



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
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends