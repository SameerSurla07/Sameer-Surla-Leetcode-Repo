#User function Template for python3

class Solution:
    
    def dfs(self, node, adj, visited):
        # Mark the current node as visited
        visited[node] = True
        # Visit all neighbors of the current node
        for neighbor in range(len(adj)):
            if adj[node][neighbor] == 1 and not visited[neighbor]:
                self.dfs(neighbor, adj, visited)
            
    def numProvinces(self, adj, V):
        
        visited = [False] * V # keep track of visited
        province_count = 0
        
        for i in range(V):
            if not visited[i]:
                province_count += 1
                self.dfs(i, adj, visited)
                
    
        return province_count
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        V=int(input())
        adj=[]
        
        for i in range(V):
            temp = list(map(int,input().split()))
            adj.append(temp);
        
        ob = Solution()
        print(ob.numProvinces(adj,V))
# } Driver Code Ends