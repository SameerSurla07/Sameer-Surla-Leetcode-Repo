class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)  # Number of node
        color = [-1] * n  # Color array initialized to -1 ( uncolored )

        def bfs( start : int) -> bool:
            queue = deque([start])
            color[start] = 0  # Start by coloring the start node with color 0

            while queue:
                node = queue.popleft()
                current_color = color[node]

                for neighbor in graph[node]:
                    if color[neighbor] == -1:  # If neighbor has not been colored
                        # Color with opposite color
                        color[neighbor] = 1 - current_color
                        queue.append(neighbor)
                    
                    elif color[neighbor] == current_color:
                        return False  # Graph is not a bipartite
                    
            return True

        # Check for all components
        for i in range(n):
            if color[i] == -1:
                if not bfs(i):
                    return False
                
        return True
