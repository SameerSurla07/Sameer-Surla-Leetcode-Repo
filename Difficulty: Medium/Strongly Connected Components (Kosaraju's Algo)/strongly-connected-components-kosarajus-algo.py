#User function Template for python3

from collections import defaultdict

class Solution:
    
    #Function to find number of strongly connected components in the graph.
    def kosaraju(self, V, adj):
        # code here
        
        # Step 1: Perform DFS on the original graph and store the
        # finish times of the nodes
        
        def dfs(node, adj, visited, stack):
            visited[node] = True
            
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    dfs(neighbor, adj, visited, stack)
                    
            stack.append(node)
            
        
        # Step 2: Transpose the graph
        
        def transpose_graph(V, adj):
            
            transposed = defaultdict(list)
            
            for node in range(V):
                for neighbor in adj[node]:
                    transposed[neighbor].append(node)
            
            return transposed
        
        
        # Step 3: Perform DFS on the transposed graph in the 
        # order of finish time
        
        def dfs_transposed(node, transposed_adj, visited):
            
            visited[node] = True
            
            for neighbor in transposed_adj[node]:
                if not visited[neighbor]:
                    dfs_transposed(neighbor, transposed_adj, visited)
    
        visited = [False] * V
        
        stack = []
        
        for i in range(V):
            if not visited[i]:
                dfs(i, adj, visited, stack)
                
        
        transposed_adj = transpose_graph(V, adj)
        
        visited = [False] * V
        
        scc_count = 0
        
        while stack:
            node = stack.pop()
            
            if not visited[node]:
                
                dfs_transposed(node, transposed_adj, visited)
                scc_count += 1
                
        return scc_count
            
            
            
            
            


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
        print("~")
# } Driver Code Ends