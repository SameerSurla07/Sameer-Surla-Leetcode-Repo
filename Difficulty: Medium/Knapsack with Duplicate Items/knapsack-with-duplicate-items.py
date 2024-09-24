#User function Template for python3

class Solution:
    def knapSack(self, N, W, val, wt):
        # code here
        
        # Create a DP table of size (n+1) x (maxCapacity+1), initialized with zeros
        dp = [[0 for _ in range(W + 1)] for _ in range(N + 1)]
        
        # Iterate through all the items
        for i in range(1, N + 1):
            # Iterate through all possible capacities
            for capacity in range(1, W + 1):
                
                # If the current item can be included (weight is less than or equal to the capacity)
                if wt[i - 1] <= capacity:
                    
                    # Option 1: Include the item and add its value, reduce the remaining capacity
                    include_item = val[i - 1] + dp[i][capacity - wt[i - 1]]
                    
                    # Option 2: Exclude the item
                    exclude_item = dp[i - 1][capacity]
                    
                    # Take the maximum of both options
                    dp[i][capacity] = max(include_item, exclude_item)
                
                else:
                    # If the item cannot be included, carry forward the value from the previous row
                    dp[i][capacity] = dp[i - 1][capacity]
        
        # The bottom-right corner of the DP table will have the maximum profit for full capacity
        return dp[N][W]
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # # Memoized Recursion
        
        # dp = [[-1 for _ in range(W + 1)] for _ in range(N+1)]

        
        # def Recursive(w, v, W, ind, memo):
            
        #     if dp[ind][W] != -1:
        #         return dp[ind][W]
            
        #     if W == 0 or ind == 0:
        #         return 0
            
        #     if w[ind-1] > W:
        #         return Recursive(w, v, W, ind - 1, dp)
        #     else:
        #         include = v[ind - 1] + Recursive(w, v, W - w[ind - 1], ind, dp)
            
        #         exclude = Recursive(w, v, W, ind - 1, dp)
        
        #         dp[ind][W] = max(include, exclude)
            
        #     return dp[ind][W]
        
        # return Recursive(wt, val, W , N, dp)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
           
        
        # recursive solution
        
        # def Recursive(w, v, W, ind):
        
        #     if W == 0 or ind == 0:
        #         return 0
            
        #     if w[ind-1] > W:
        #         return Recursive(w, v, W, ind - 1)
        
        #     include = v[ind - 1] + Recursive(w, v, W - w[ind - 1], ind)
        
        #     exclude = Recursive(w, v, W, ind - 1)
        
        #     return max(include, exclude)
        
        # return Recursive(wt, val, W , N)


















#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, W = [int(x) for x in input().split()]
        val = input().split()
        for itr in range(N):
            val[itr] = int(val[itr])
        wt = input().split()
        for it in range(N):
            wt[it] = int(wt[it])
        
        ob = Solution()
        print(ob.knapSack(N, W, val, wt))
# } Driver Code Ends