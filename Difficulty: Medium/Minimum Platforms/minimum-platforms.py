#User function Template for python3

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        # code here
        
        # Sort arrival and departure times
        arr.sort()
        dep.sort()

        # Initialize variables
        platforms_needed = 0
        max_platforms = 0
        i = 0
        j = 0
    
        # Traverse through all arrival and departure times
        while i < n and j < n:
            # If next event is arrival, increment count of platforms needed
            if arr[i] <= dep[j]:
                platforms_needed += 1
                i += 1
            # If next event is departure, decrement count of platforms needed
            else:
                platforms_needed -= 1
                j += 1
            
            # Update maximum platforms needed
            max_platforms = max(max_platforms, platforms_needed)
        
        return max_platforms
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        arrival = list(map(int, input().strip().split()))
        departure = list(map(int, input().strip().split()))
        ob=Solution()
        print(ob.minimumPlatform(n,arrival,departure))
# } Driver Code Ends