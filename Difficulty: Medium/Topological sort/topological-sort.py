from collections import deque, defaultdict

class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here
        
        # Kahn's Algorithms ( Like BFS )
        # this approach uses indegree of nodes and adds nodes 
        # with indegree 0 to the queue and then visits its
        # neighbors and then does the same with them
        
        # Step 1: Initialize in-degree of all vertices to 0
        in_degree = [0] * V
        
        # Step 2: Calculate indegree of each node
        for u in range(V):  # for elements in adj
            for v in adj[u]:  # for elemetns in adj[u]
                in_degree[v] += 1
    
        # Step 3: Initialize a queue and enqueue all vertices with in-degree 0
        queue = deque()
        for i in range(V):
            if in_degree[i] == 0:
                queue.append(i)
        
        # Step 4: Initialize an empty list to store the topological sort order
        topo_order = []
        
        # Step 5: Process the queue
        while queue:
            # Deque a vertex with in-degree 0 and add it to topo_order
            u = queue.popleft()
            topo_order.append(u)
            
            # Decrease the in-degree of all adjacent vertices as it is now removed from queue
            for v in adj[u]:
                in_degree[v] -= 1
                # If in-degree become 0, add it to the queue
                if in_degree[v] == 0:
                    queue.append(v)
            
        # Step 6: Check if the topological sort contains all vertices
        if len(topo_order) == V:
            return topo_order
        else:
            # If not, there was a cycle (but per problem constraints, this won't happen)
            return []

    

        
        
        # DFS Approach ( Recuresive - but space efficient)

        # visited = [False] * V  # Keep track of visited nodes
        # stack = []  # To store topological order
        
        # def dfs(node:int):
        #     visited[node] = True
            
        #     # Visit all adj nodes (children) of current node
        #     for neighbor in adj[node]:
        #         if not visited[neighbor]:
        #             dfs(neighbor)
                
        #     # Add the node to the stack once all its descendants are processed
        #     stack.append(node)
            
        
        # # Perform DFS for all unvisited ndoes
        # for i in range(V):
        #     if not visited[i]:
        #         dfs(i)
            
        # return stack[::-1]

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