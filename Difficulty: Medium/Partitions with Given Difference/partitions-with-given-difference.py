
from typing import List
MOD = 10**9 + 7

class Solution:
    def countPartitions(self, n : int, d : int, arr : List[int]) -> int:
        # code here
        MOD = 10 ** 9 + 7
        
        # Approach 4: Space optmization
        
        total_sum = sum(arr)
        
        if (total_sum + d) % 2 == 1 or total_sum < d:
            return 0
            
        S1 = (total_sum + d) // 2

        # Create a 1D DP array to store the number of ways to pick subsets that sum to j
        dp = [0] * ( S1 + 1 )
        
        # Base case: Number of ways to get sum 0
        dp[0] = 1
        
        # Fill the DP array
        for i in range(n):
            # We need to iterate backwards to ensure that each element is only counted once
            for j in range(S1, arr[i] - 1, -1):
                dp[j] = ( dp[j] + dp[j-arr[i]]) % MOD
                
        return dp[S1]
        
        
        
        
        
        
        
        
        # # Approach 3: Tabulation Method
            
        # total_sum = sum(arr)
        
        # # Check if (total_sum + d) is even and if it's possible to partition
        # if (total_sum + d) % 2 != 0 or total_sum < d:
        #     return 0

        # S1 = (total_sum + d) // 2

        # # Create a 2D DP array
        # # dp[i][j] stores the number of ways to pick subsets 
        # # from the first i elements such that
        # # their sum equals j.
        
        
        # # Base case 2: If S1 is zero, we need to check how many subsets can make sum zero.
        # if S1 == 0:
        #     # If all elements are zero, we have 2^n subsets (as each element can either be chosen or not).
        #     return 2**n % MOD

            
        # dp = [[0] * (S1+1) for _ in range(n + 1)]

        # # Base case: there's one way to make sum 0 (empty subset)
        # for i in range(n + 1):
        #     dp[i][0] = 1

        # # Fill the dp table
        # for i in range(1, n+1):
        #     for j in range(S1 + 1):
        #         # Don't include arr[i-1]
        #         dp[i][j] = dp[i-1][j]
                
        #         # Include arr[i-1] if it's not larger than current sum
        #         if arr[i-1] <= j:
        #             dp[i][j] = (dp[i][j] + dp[i-1][j - arr[i-1]]) % MOD
        
        # return dp[n][S1]

        
        
        
        
        
        
        
        
        
        
        
        
        # # Approach 2: Momized Recursive
        
        # def findWays(ind, S1, total_sum, memo):
            
        #     if ind == n:
        #         S2 = total_sum - S1
        #         if S1 - S2 == d:
        #             return 1
        #         else:
        #             return 0
                    
        #     if (ind, S1) in memo:
        #         return memo[(ind, S1)]
                
        #     include = findWays(ind + 1, S1 + arr[ind], total_sum, memo)
            
        #     exclude = findWays(ind + 1, S1, total_sum, memo)
            
        #     memo[(ind, S1)] = ( include + exclude ) % MOD
            
        #     return memo[(ind, S1)]
            
        # total_sum = sum(arr)
        # memo = {}
        
        # return findWays(0, 0, total_sum, memo)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # Approach 1: recursive
        # def findWays(ind, S1, total_sum):
        #     if ind == n:
        #         S2 = total_sum - S1
        #         if S1 - S2 == d:
        #             return 1
        #         else:
        #             return 0
                    
            
        #     include = findWays(ind + 1, S1 + arr[ind], total_sum)
            
        #     exclude = findWays(ind + 1, S1, total_sum)
            
        #     return (include + exclude) % MOD
            
        # total_sum = sum(arr)
        
        # return findWays(0, 0, total_sum)        
        
        
        
        



#{ 
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        d = int(input())
        
        
        arr=IntArray().Input(n)
        
        obj = Solution()
        res = obj.countPartitions(n, d, arr)
        
        print(res)
        

# } Driver Code Ends