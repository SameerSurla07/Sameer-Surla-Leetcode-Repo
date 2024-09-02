#User function Template for python3
from typing import List

class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V : int , adj : List[List[int]]) -> bool :
        # code here
        def dfs(node):
            visited[node] = True
            recStack[node] = True
            
            for neighbor in adj[node]:
                if not visited[neighbor]:  # If neighbor hasn't been visited yet, do a DFS on it
                    if dfs(neighbor):
                        return True
                        
                elif recStack[neighbor]:  # If neighbor is in recStack, there is a cycle
                    return True
            
            recStack[node] = False  # Remove the node from recursion stack before returning
            return False


        visited = [False] * V
        recStack = [False] * V
        
        for i in range(V):
            if not visited[i]:
                if dfs(i):
                    return True
        
        return False
















































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