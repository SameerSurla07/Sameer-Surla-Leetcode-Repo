#User function Template for python3
from typing import List
from collections import deque

class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V : int , adj : List[List[int]]) -> bool :
        # code here
        
        # BFS Approach - Kahn's Algorithm
        
        # Step 1: Initialize an in-degree array with 0
        in_degree = [0] * V
        
        # Step 2: Calculate in-degree of each vertex
        for u in range(V):
            for v in adj[u]:
                in_degree[v] += 1
            
        # Step 3: Initialize a queue and enqueue all 
        # vertices with in-degree 0
        queue = deque()
        for u in range(V):
            if in_degree[u] == 0:
                queue.append(u)
            
        # Step 4: Initialize a count for the number of processed vertices
        count = 0
    
        # Step 5: Process the queue
        while queue:
            # Dequeue a vertex with in-degree 0
            u = queue.popleft()
            count += 1
            
            # Decrease the in-degree of all adjacent vertices
            for v in adj[u]:
                in_degree[v] -= 1
                
                # If in-degree becomes 0, add it to the queue
                if in_degree[v] == 0:
                    queue.append(v)
                    
        # Step 6: If count equals V, then the graph is acyclic (no cycle)
        if count == V:
            return False  # No cycle detected
        else:
            return True  # Cycle detected

        
        
        
        
        
        
        
        
        
        
        
        
        # DFS approach
        
        # Uses visited and path-visited(recursive Stack)
        # Essentially checks if the node which is already visited
        # is there in our current path or not, if it is, 
        # then it's a cycle
        
        # def dfs(node):
        #     visited[node] = True
        #     recStack[node] = True
            
        #     for neighbor in adj[node]:
        #         if not visited[neighbor]:  # If neighbor hasn't been visited yet, do a DFS on it
        #             if dfs(neighbor):
        #                 return True
                        
        #         elif recStack[neighbor]:  # If neighbor is in recStack, there is a cycle
        #             return True
            
        #     recStack[node] = False  # Remove the node from recursion stack before returning
        #     return False


        # visited = [False] * V
        # recStack = [False] * V
        
        # for i in range(V):
        #     if not visited[i]:
        #         if dfs(i):
        #             return True
        
        # return False
















































#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V, E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a, b = map(int, input().strip().split())
            adj[a].append(b)
        ob = Solution()

        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)

# } Driver Code Ends