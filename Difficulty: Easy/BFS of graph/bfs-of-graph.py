#User function Template for python3

from typing import List
from queue import Queue
# Importing deque from the collections module
from collections import deque

class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # List to store the BFS traversal order
        bfs = []
        
        # Visited list to keep track of visited nodes
        visited = [False] * V
        
        # Queue to manage the BFS order, starting with node 0
        q = deque([0])
        
        # Mark the starting node (0) as visited
        visited[0] = True
        
        # Loop until the queue is empty
        while q:
            # Pop the first element from the queue (FIFO)
            node = q.popleft()
            
            # Add the current node to the BFS result
            bfs.append(node)
            
            # Check all neighbors of the current node
            for neighbor in adj[node]:  # Here, neighbor is an integer
                # If the neighbor hasn't been visited yet
                if not visited[neighbor]:
                    # Add the neighbor to the queue for future exploration
                    q.append(neighbor)
                    
                    # Mark the neighbor as visited
                    visited[neighbor] = True
        
        # Return the BFS traversal order as a list
        return bfs
            
            
            
            

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
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends