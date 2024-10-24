#{ 
 # Driver Code Starts
# Initial Template for Python 3
import atexit
import io
import sys
import heapq
from typing import List, Tuple


# } Driver Code Ends

import heapq

class Solution:
    # Function to find the shortest distance of all the vertices
    # from the source vertex src.
    def dijkstra(self, adj: List[List[Tuple[int, int]]], src: int) -> List[int]:
        # Your code here
        
        V = len(adj)
        
        # Step 1: Initialize distance array and priority queue
        dist = [float('inf')] * V
        
        dist[src] = 0
        
        pq = [(0, src)]  # (dist from source, vertex)
        
        
        # Step 2: Process the vertices in order of their current known shortest distance
        
        while pq:
            
            current_dist, node = heapq.heappop(pq)
            
            if current_dist > dist[node]:
                continue
            
            for neighbor, weight in adj[node]:
                
                distance = current_dist + weight
                
                if distance < dist[neighbor]:
                    dist[neighbor] = distance
                    
                    heapq.heappush(pq, (distance, neighbor))
                    
        return dist
        
        
        
        
        
        
        

#{ 
 # Driver Code Starts.

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V, E = map(int, input().strip().split())
        adj = [[] for _ in range(V)]
        for _ in range(E):
            u, v, w = map(int, input().strip().split())
            adj[u].append((v, w))
            adj[v].append((u, w))
        src = int(input())
        ob = Solution()

        res = ob.dijkstra(adj, src)
        for i in res:
            print(i, end=" ")
        print()
# } Driver Code Ends