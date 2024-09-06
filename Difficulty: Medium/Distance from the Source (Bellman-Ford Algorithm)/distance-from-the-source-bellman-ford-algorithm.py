#User function Template for python3
import heapq
from heapq import heappop, heappush

class Solution:
    # Function to construct and return cost of MST for a graph
    # represented using adjacency matrix representation
    '''
    V: nodes in graph
    edges: adjacency list for the graph
    S: Source
    '''
    def bellman_ford(self, V, edges, S):
        #code here
        
        # Initialize distance array with 10^8
        distances = [10**8] * V
        distances[S] = 0
        
        # Relax all V-1 edges
        for _ in range(V-1):
            for u, v, w in edges:
                if distances[u] != 10**8 and distances[u] + w < distances[v]:
                    distances[v] = distances[u] + w
                    
        
        # Check for negative cycles
        for u, v, w in edges:
            if distances[u] != 10**8 and distances[u] + w < distances[v]:
                return [-1]
        
        return distances
            
        
        
        
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        edges = []
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            edges.append([u,v,w])
        S=int(input())
        ob = Solution()
        
        res = ob.bellman_ford(V,edges,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends