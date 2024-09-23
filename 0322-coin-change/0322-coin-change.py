class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # Tabulation Solution

        n = len(coins)

        dp = [[0 for _ in range(amount + 1)] for _ in range(n)]
        # Fill in the DP table for the first element in the array ( Base case )
        for i in range(amount + 1):
            if i % coins[0] == 0:
                dp[0][i] = i // coins[0]
            else:
                dp[0][i] = float('inf')

        for ind in range(1, n):
            for target in range(amount + 1):
                
                not_take = dp[ind -1][target]

                take = float('inf')

                if coins[ind] <= target:
                    take = 1 + dp[ind][target - coins[ind]]

                dp[ind][target] = min(not_take, take)

        result = dp[n-1][amount] 

        if result != float('inf'):
            return result
        else:
            return -1      
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # # Memoization Solution
        # def Recursive(ind, target, coins, dp):
        
        #     # we will start from end of coins till it's start as the base case

        #     # base case: if we have reached the start of the array
        #     if ind == 0:
        #         if target % coins[0] == 0:
        #             return target // coins[0]
        #         else:
        #             return float('inf')

        #     if dp[ind][target] != -1:
        #         return dp[ind][target]

        #     not_taken = 0 + Recursive(ind -1, target, coins, dp)

        #     taken = float('inf')

        #     if coins[ind] <= target:
        #         taken = 1 + Recursive(ind, target - coins[ind], coins, dp)

        #     dp[ind][target] = min ( not_taken, taken)

        #     return dp[ind][target]

        # n = len(coins)
        # dp = [[-1 for j in range(amount + 1)] for i in range(n)]

        # result = Recursive(n -1 , amount, coins, dp)

        # if result != float('inf'):
        #     return result
        # else:
        #     return -1


        
