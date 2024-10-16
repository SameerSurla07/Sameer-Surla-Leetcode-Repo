from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
        
        visited = [False] * V
        
        def dfs(node, parent):
            
            visited[node] = True
            
            # Visit all neighbors
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    if dfs(neighbor, node):
                        return True
                
                elif neighbor != parent:
                    return True
                    
            return False
            
        # Perform DFS for each unvisited vertex
        for i in range(V):
            if not visited[i]:
                if dfs(i, -1):
                    return 1
                    
        return 0
                    
                    







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