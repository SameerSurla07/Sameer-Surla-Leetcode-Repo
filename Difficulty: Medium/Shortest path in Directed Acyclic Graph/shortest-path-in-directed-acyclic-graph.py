#User function Template for python3
from collections import deque, defaultdict

from typing import List

class Solution:
    def shortestPath(self, n : int, m : int, edges : List[List[int]]) -> List[int]:
        
        # in edges list, for each element, 1st is from node,
        # 2nd is to node, 3rd is the edge weight

        # Step 1: Initialize adjacency list and in_degree array
        
        graph = defaultdict(list)
        in_degree = [0] * n
        
        # Step 2: Build the adjacency list and in_degree array
        
        for u, v, w in edges:
            graph[u].append((v, w))  # from node, to node, weight
            in_degree[v] += 1

        # Step 3: initialize queue and populate it
        
        queue = deque()
        for node in range(n):
            if in_degree[node] == 0:
                queue.append(node)
                
        # Step 4: Initialize topo_array
        topo_order = []
        
        # Step 5: Process the queue using Kahn's Algorithm
        while queue:
            current = queue.popleft()  # It has in_degree 0
            topo_order.append(current)
            
            # Decrease in_degree of adjacent node
            for neighbor,_ in graph[current]:
                in_degree[neighbor] -= 1
                # If in_degree becomes zero, append it to queue
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                
        # Step 6: Initialize distance array
        dist = [float('inf')] * n
        dist[0] = 0
        
        # Step 7: Process nodes in topological order and relax edges
        for node in topo_order:
            if dist[node] != float('inf'):
                for neighbor, weight in graph[node]:
                    if dist[node] + weight < dist[neighbor]:
                        dist[neighbor] = dist[node] + weight
        
        # Step 8: Return distance array
        return [d if d != float('inf') else -1 for d in dist]















#{ 
 # Driver Code Starts

#Initial Template for Python 3

from typing import List




class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()



class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n,m=map(int,input().split())
        
        
        edges=IntMatrix().Input(m, 3)
        
        obj = Solution()
        res = obj.shortestPath(n, m, edges)
        
        IntArray().Print(res)
# } Driver Code Ends