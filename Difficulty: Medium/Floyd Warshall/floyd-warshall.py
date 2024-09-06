#User function template for Python

class Solution:
	def shortest_distance(self, matrix):
		#Code here

        # Number of vertices
        n = len(matrix)
        
        # Step 1: Initialize the matrix by replacing -1 
        # with infinity where no direct edge exits
        INF = float('inf')
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == -1 and i != j:
                    matrix[i][j] = INF
                    
        # Step 2: Floyd-Warshall Algorithm (considering 
        # each vertex as an intermediate)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    # If the path through vertex k is shorter,
                    # update the path
                    if matrix[i][k] != INF and matrix[k][j] != INF:
                        matrix[i][j] = min ( matrix[i][j], matrix[i][k] + matrix[k][j] )
                        
        # Step 3: Convert 'infinity' back to -1 where no path exists
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == INF:
                    matrix[i][j] = -1
        
















#{ 
 # Driver Code Starts
#Initial template for Python 

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		matrix = []
		for _ in range(n):
			matrix.append(list(map(int, input().split())))
		obj = Solution()
		obj.shortest_distance(matrix)
		for _ in range(n):
			for __ in range(n):
				print(matrix[_][__], end = " ")
			print()
# } Driver Code Ends