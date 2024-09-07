#User function Template for python3
from typing import List
import heapq
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V: int, adj: List[List[int]]) -> int:
        #code here
        
        # Kruskal's Algorithm
        
        # Helper Class for Disjoint Set Union (Union Find)
        class DSU:
            def __init__(self, n):
                # Initialize parent array and rank for union-find operations
                self.parent = list(range(n))  # Parent array for union-find
                self.rank = [0] * n  # Rank array to keep track of tree heights
                
            def find(self, u):
                # Path compression optimization
                if self.parent[u] != u:
                    self.parent[u] = self.find(self.parent[u])
                return self.parent[u]
                
            def union(self, u, v):
                # Union by rank optimization
                root_u = self.find(u)
                root_v = self.find(v)
                
                if root_u != root_v:
                    # Attach the smaller tree under the root of the larger tree
                    if self.rank[root_u] < self.rank[root_v]:
                        self.parent[root_u] = root_v

                    elif self.rank[root_u] > self.rank[root_v]:
                        self.parent[root_v] = root_u
                        
                    else:
                        self.parent[root_v] = root_u
                        self.rank[root_u] += 1
            
        # Step 1: Create a list of all edges in the format (weight, u, v)
        edges = []
        for u in range(V):
            for v, weight in adj[u]:
                edges.append((weight, u, v))
                
        # Step 2: Sort edges by weight ( ascending order )
        edges.sort()
        
        # Stpe 3: Initialze the Disjoint Set Union ( DSU )
        dsu = DSU(V)
        
        # Step 4: Kruskal's Algo to find MST
        # To store the sum of weights of the MST edges
        mst_weight = 0  
        # Top ensure we stop after adding V-1 edges to the MST
        edge_count = 0
        
        for weight, u, v in edges:
            # Step 5: USe union-find to avoid cycles
            if dsu.find(u) != dsu.find(v):
                dsu.union(u,v)
                mst_weight += weight
                edge_count += 1
                
                # Stop early if we have V-1 edges in MST
                if edge_count == V-1:
                    break
        
        return mst_weight
        
        
        
        
        
        
        
        
        
        # # Prim's Algorithm
        
        # # priority queue to store edges based on their weights
        # pq = []
        
        # # To keep track of vertices included in MST
        # inMST = [False] * V
        
        # # initialize with vertex 0, pushing all edges 
        # # connected to it into pq
        # heapq.heappush(pq, (0,0))  # (weight, vertex)
        
        # total_weight = 0  # To accumulate weight of MST
        # edges_in_mst = 0  # Track number of edges added to MST
        
        # # Prim's Algo to find the MST
        # while pq and edges_in_mst <= (V - 1) :
        #     # Prick the edge with smallest weight
        #     weight, u = heapq.heappop(pq)
            
        #     # If vertex is already included in MST, skip it
        #     if inMST[u]:
        #         continue
            
        #     # Mark the vertex as part of MST
        #     inMST[u] = True
        #     # Add the edge weight to total weight
        #     total_weight += weight  
        #     # Increment the edge count in MST
        #     edges_in_mst += 1
            
        #     # Explore all adjacent vertices of the current vertex u
        #     for neighbor, edge_weight in adj[u]:
        #         # Only consider edges to vertices not in MST
        #         if not inMST[neighbor]:
        #             heapq.heappush(pq, (edge_weight, neighbor))
                
        # return total_weight











#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
from typing import List

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V, E = map(int, input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u, v, w = map(int, input().strip().split())
            adj[u].append([v, w])
            adj[v].append([u, w])
        ob = Solution()

        print(ob.spanningTree(V, adj))

# } Driver Code Ends