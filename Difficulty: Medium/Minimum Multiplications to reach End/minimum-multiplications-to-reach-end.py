#User function Template for python3

from typing import List
from collections import deque
 
class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        # code here
        
        # Step 1: If start and end is same, then no steps are required
        if start == end:
            return 0
            
        MOD = 100000
        visited = [-1] * MOD  # Initializing visited array
        visited[start] = 0  # Mark the starting point as visited with 0 steps
        
        # Step 2: BFS queue initialized with ( start_value, steps_taken)
        
        queue = deque ([(start, 0)])
        
        # Step 3: Handle queue
        
        while queue:
            current, steps = queue.popleft()
            
            # Step 4: Try multiplying by each number in ar and take MOD
            
            for multiplier in arr:
                new_value = (current * multiplier) % MOD
                
                # if we reach end, return steps + 1
                if new_value == end:
                    return steps + 1
                
                # If the new value is not visited yet, add it to the queue
                if visited[new_value] == -1:
                    visited[new_value] = steps + 1  # Mark it visited with new steps count
                    queue.append((new_value, steps + 1))
        
        
        # Step 5: If we exhaust the queue and don't reach the end, return -1 
        return -1
                
        







#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        start, end = list(map(int,input().split()))
        obj=Solution()
        print(obj.minimumMultiplications(arr, start, end))
# } Driver Code Ends