#User function Template for python3

class Solution:
    #Function to count number of ways to reach the nth stair.
    def countWays(self,n):
        MOD = 10**9 + 7
        
        # code here
        # Bottom Up approach - tabulation
        if n == 1:
            return 1
        if n == 2:
            return 2
            
        # initialize the first two steps
        # dp[1] is 1 way 
        # dp[2] is 2 ways
        
        a, b = 1, 2
        
        for i in range(3, n+1):
            a, b = b, (a+b) % MOD
            
            
        return b
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
sys.setrecursionlimit(10**6)

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m = int(input())
        ob=Solution()
        print(ob.countWays(m))

# } Driver Code Ends