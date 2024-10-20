class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topologicalSort(self,adj):
        # Code here
        
        # DFS 
        
        # We will add a node to final result only when 
        # all his neighbors have been visited and then
        # at the end, reverse it
        V = len(adj)
        
        visited = [False] * V  # Track visited nodes
        result = []  # array to store the topological sort
        
        def dfs(v):
            visited[v] = True
            
            # Visit all neighbors
            for neighbor in adj[v]:
                if not visited[neighbor]:
                    dfs(neighbor)
                    
            result.append(v)
            
        for i in range(V):
            if not visited[i]:
                dfs(i)
                
        return result[::-1]
        
        
#{ 
 # Driver Code Starts
# Driver Program

import sys

sys.setrecursionlimit(10**6)


def check(graph, N, res):
    if N != len(res):
        return False
    map = [0] * N
    for i in range(N):
        map[res[i]] = i
    for i in range(N):
        for v in graph[i]:
            if map[i] > map[v]:
                return False
    return True


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        e, N = list(map(int, input().strip().split()))
        adj = [[] for i in range(N)]

        for i in range(e):
            u, v = map(int, input().split())
            adj[u].append(v)

        ob = Solution()

        res = ob.topologicalSort(adj)

        if check(adj, N, res):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

# } Driver Code Ends