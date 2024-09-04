from typing import List
import heapq
class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V: int, adj: List[List[int]], S: int) -> List[int]:
        # Code here
        
        # Step 1: Initialize distance array
        dist = [float('inf')] * V
        dist[S] = 0  # Disatance to the source vertex is 0
        
        # Step 2: Priority Queue for Dijkstra's algorithm
        min_heap = [(0,S)]  # (distance, vertex)
        
        # Step 3: Process the priority Queue
        while min_heap:
            # Get the vertex with the smallest distance
            current_dist, u = heapq.heappop(min_heap)
            
            # If the popped vertex distance is greater
            # than the recorded distance, skip it
            if current_dist > dist[u]:
                continue
            
            # Process all neighbors of vertex u
            for v, weight in adj[u]:
                # Calculate new distance
                distance = current_dist + weight 
                
                # If a shorter path is found, update the
                # distance and push to the priority queue
                if distance < dist[v]:
                    dist[v] = distance
                    heapq.heappush(min_heap, (distance, v))
                    
        # Convert 'inf' to -1 for vertices that are unreachable
        return [d if d != float('inf') else -1 for d in dist]
















#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V, E = map(int, input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u, v, w = map(int, input().strip().split())
            adj[u].append([v, w])
            adj[v].append([u, w])
        S = int(input())
        ob = Solution()

        res = ob.dijkstra(V, adj, S)
        for i in res:
            print(i, end=" ")
        print()

# } Driver Code Ends