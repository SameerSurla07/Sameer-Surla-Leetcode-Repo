class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here

        visited = [False] * V  # Keep track of visited nodes
        stack = []  # To store topological order
        
        def dfs(node:int):
            visited[node] = True
            
            # Visit all adj nodes (children) of current node
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    dfs(neighbor)
                
            # Add the node to the stack once all its descendants are processed
            stack.append(node)
            
        
        # Perform DFS for all unvisited ndoes
        for i in range(V):
            if not visited[i]:
                dfs(i)
            
        return stack[::-1]

#{ 
 # Driver Code Starts
# Driver Program

import sys
sys.setrecursionlimit(10**6)
        
def check(graph, N, res):
    if N!=len(res):
        return False
    map=[0]*N
    for i in range(N):
        map[res[i]]=i
    for i in range(N):
        for v in graph[i]:
            if map[i] > map[v]:
                return False
    return True

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        e,N = list(map(int, input().strip().split()))
        adj = [[] for i in range(N)]
        
        for i in range(e):
            u,v=map(int,input().split())
            adj[u].append(v)
            
        ob = Solution()
        
        res = ob.topoSort(N, adj)
        
        if check(adj, N, res):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

# } Driver Code Ends