#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:
    def minimizeCost(self, arr, k):
        # code here
        n = len(arr)
        dp = [float('inf')] * n
        
        if n == 1:
            return 0
        
        dp[0] = 0   # No cost to start at the first stone
        
        # Loop through each stone starting from the second one
        for i in range(1, n):
            # Check all possible jumps from i-1 to i-k (within bounds)
            for j in range(1, k+1):
                if i - j >= 0:
                    jump = dp[i-j] + abs(arr[i] - arr[i-j])
                    dp[i] = min(dp[i], jump)
            
        return dp[n-1]
        
        
        
        
        
        
        
        
        
        

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        k= int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.minimizeCost(arr,k)
        print(res)
        t -= 1


# } Driver Code Ends