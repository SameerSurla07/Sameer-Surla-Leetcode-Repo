class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Initialize the distance matrix with infinity
        dist = [[float('inf')] * n for _ in range(n)]

        # Distance from a city to itself is 0
        for i in range(n):
            dist[i][i] = 0

        # Populate the distance matrix with the given edges
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w

        # Floyd-Warshall algorithm to compute shortest paths
        for k in range(n):  # Intermediate node is k
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:  # i to k , then k to j
                        dist[i][j] = dist[i][k] + dist[k][j]

        # Find the city with the smallest number of reachable cities within the threshold
        minReachable = n
        bestCity = -1
        for i in range(n):
            reachableCount = sum(1 for j in range(n) if dist[i][j] <= distanceThreshold)
            if reachableCount < minReachable or (reachableCount == minReachable and i > bestCity):
                minReachable = reachableCount
                bestCity = i
        
        return bestCity