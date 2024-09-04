#User function Template for python3
from collections import deque, defaultdict

class Solution:
    def shortestPath(self, edges, n, m, src):
        # code here
        
        # Step 1: Create an adjacency list from the edges
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)  # Undirected Graph
        
        # Step 2: Initialize the distance array
        distance = [-1] * n
        distance[src] = 0
        
        # Step 3: BFS to calculate the shortest paths
        queue = deque([src])
        
        while queue:
            node = queue.popleft()
            
            # Explore all adjacent neighbors
            for neighbor in graph[node]:
                if distance[neighbor] == -1:  # Unvisited
                    distance[neighbor] = distance[node] + 1
                    queue.append(neighbor)
                    

        return distance












#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = map(int, input().strip().split())
        edges=[]
        for i in range(m):
            li=list(map(int,input().split()))
            edges.append(li)
        src=int(input())
        ob = Solution()
        ans = ob.shortestPath(edges,n,m,src)
        for i in ans:
            print(i,end=" ")
        print()
        tc -= 1
# } Driver Code Ends