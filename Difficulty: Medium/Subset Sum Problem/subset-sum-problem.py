#User function Template for python3

class Solution:
    def isSubsetSum (self, N, arr, sum):
        # code here 
        
        
        
        # Memoization Approach
        
        dp = [[-1 for _ in range(sum + 1)] for _ in range(N+1)]
        
        def subsetSum(n, arr, sum):
            # Base cases
            if sum == 0:
                return True
            if n == 0:
                return False
                
            if dp[n][sum] != -1:
                return dp[n][sum]
                
            # If element is greater than the remaining sum,
            # we can't include it
            if arr[n-1] > sum:
                dp[n][sum] = subsetSum(n-1, arr, sum)
            else:
                dp[n][sum] = subsetSum(n-1, arr, sum) or subsetSum(n-1, arr, sum - arr[n-1])
                
            return dp[n][sum]
            
        return subsetSum(N, arr, sum)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        sum = int(input())

        ob = Solution()
        if ob.isSubsetSum(N,arr,sum)==True:
            print(1)
        else :
            print(0)
            
        

# } Driver Code Ends