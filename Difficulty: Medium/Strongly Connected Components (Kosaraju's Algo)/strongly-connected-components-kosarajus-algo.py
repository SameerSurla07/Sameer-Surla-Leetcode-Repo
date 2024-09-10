#User function Template for python3
from collections import defaultdict

class Solution:
    
    #Function to find number of strongly connected components in the graph.
    def kosaraju(self, V, adj):
        # code here

        # Step 1: Perform DFS on original graph to get 
        # finishing times
        def dfs1(node, visited, stack):
            visited[node] = True
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    dfs1(neighbor, visited, stack)
            # Push the node to stack after visiting all its neighbors
            stack.append(node)

        # Transpose the graph
        def transpose_graph(adj, V):
            transpose_adj = defaultdict(list)
            for u in range(V):
                for v in adj[u]:
                    transpose_adj[v].append(u)  # Reverse the edge
            return transpose_adj
        
        # Step 2: Perform DFS on the transposed graph
        def dfs2(node, visited, transpose_adj, component):
            visited[node] = True
            component.append(node)
            for neighbor in transpose_adj[node]:
                if not visited[neighbor]:
                    dfs2(neighbor, visited, transpose_adj, component)
            
        
        # Step 1: DFS on original graph to fill the stack 
        # based on finishing times
        visited = [False] * V
        stack = []
        for i in range(V):
            if not visited[i]:
                dfs1(i, visited, stack)
                
        # Step 2: Transpose the graph
        transpose_adj = transpose_graph(adj, V)
        
        # Step 3: Perform DFS on the transposed graph in order of
        # decreasing finishing times
        visited = [False] * V
        sccs = []  # Store the strongly connectd components
        while stack:
            node = stack.pop()
            if not visited[node]:
                component = []
                dfs2(node, visited, transpose_adj, component)
                sccs.append(component)
                
        return len(sccs)













#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import OrderedDict 
import sys 

sys.setrecursionlimit(10**6) 
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        print(ob.kosaraju(V, adj))
# } Driver Code Ends