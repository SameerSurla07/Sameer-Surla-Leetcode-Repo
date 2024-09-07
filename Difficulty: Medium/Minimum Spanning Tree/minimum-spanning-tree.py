#User function Template for python3
from typing import List
import heapq
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V: int, adj: List[List[int]]) -> int:
        #code here
        
        # priority queue to store edges based on their weights
        pq = []
        
        # To keep track of vertices included in MST
        inMST = [False] * V
        
        # initialize with vertex 0, pushing all edges 
        # connected to it into pq
        heapq.heappush(pq, (0,0))  # (weight, vertex)
        
        total_weight = 0  # To accumulate weight of MST
        edges_in_mst = 0  # Track number of edges added to MST
        
        # Prim's Algo to find the MST
        while pq and edges_in_mst <= (V - 1) :
            # Prick the edge with smallest weight
            weight, u = heapq.heappop(pq)
            
            # If vertex is already included in MST, skip it
            if inMST[u]:
                continue
            
            # Mark the vertex as part of MST
            inMST[u] = True
            # Add the edge weight to total weight
            total_weight += weight  
            # Increment the edge count in MST
            edges_in_mst += 1
            
            # Explore all adjacent vertices of the current vertex u
            for neighbor, edge_weight in adj[u]:
                # Only consider edges to vertices not in MST
                if not inMST[neighbor]:
                    heapq.heappush(pq, (edge_weight, neighbor))
                
        return total_weight











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