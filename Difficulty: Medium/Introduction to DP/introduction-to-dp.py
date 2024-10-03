#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    
    MOD = 10 ** 9 + 7
    def topDown(self, n):
        # Code here
        dp = [-1] * (n + 1)
        def recursive(n):
            if n == 1:
                return 1
            if n == 0:
                return 0
            
            if dp[n] != -1:
                return dp[n]
            
            first = recursive(n - 1)
            second = recursive(n - 2)
            
            dp[n] =  (first + second) % self.MOD 
        
            return dp[n]
            
        return recursive(n)
            
        
    def bottomUp(self, n):
        # Code here
    
        if n == 1:
            return 1
        if n == 0:
            return 0
        n2 = 0
        n1 = 1
        result = 0
        
        for i in range(2, n + 1):
            result = (n1 + n2) % self.MOD
            n2, n1 = n1, result
        
        return result
        

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n = int(input())
        ob = Solution()
        topDownans=ob.topDown(n);
        bottomUpans=ob.bottomUp(n);
        if(topDownans!=bottomUpans):
            print(-1)
        else:
            print(bottomUpans)
# } Driver Code Ends