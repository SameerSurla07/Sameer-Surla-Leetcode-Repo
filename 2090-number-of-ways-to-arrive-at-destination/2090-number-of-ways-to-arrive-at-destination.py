class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        
        # Step 1: Build the graph using an adjacency list representation
        graph = { i: [] for i in range(n)}
        for u,v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))

        # step 2: Initialize distance table and path count arrays
        # Shortest time to each node
        dist = [float('inf')] * n
        dist[0] = 0  # starting at node 0

        # number of ways to each node in the shortest time 
        ways = [0] * n
        ways[0] = 1  # Only 1 way to be at the start node

        # Step 3: Min-heap to process nodes by shortest distance first
        pq = [(0, 0)]  # (distance, node), starting with node 0

        # Step 4: Perform dijkstra's algorithm
        while pq:
            current_dist, node = heapq.heappop(pq)

            # Skip processing if this is a stale distance
            if current_dist > dist[node]:
                continue
            
            # Process each neighbor of the current node
            for neighbor, travel_time in graph[node]:
                new_dist = current_dist + travel_time

                # if we find a shorter path to the neighbor, update the distance
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    # Reset the number of ways
                    ways[neighbor] = ways[node]
                    heapq.heappush(pq, (new_dist, neighbor))

                # If we find another shortest path to the neighbor, add the ways
                elif new_dist == dist[neighbor]:
                    ways[neighbor] = ( ways[neighbor] + ways[node] ) % ( 10 ** 9 + 7)
                

        return ways[n-1] if dist[n-1] != float('inf') else 0