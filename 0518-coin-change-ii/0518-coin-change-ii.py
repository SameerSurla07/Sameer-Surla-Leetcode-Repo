class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        # Tabulation solution

        n = len(coins)

        dp = [[0 for _ in range(amount + 1)] for _ in range(n)] 

        # Initialize the base condition for the first element in the array
        for i in range(amount + 1):
            if i % coins[0] == 0:
                dp[0][i] = 1
   
        for ind in range(1, n):
            for target in range(amount + 1):

                not_taken = dp[ind - 1][target]

                taken = 0
                if coins[ind] <= target:
                    taken = dp[ind][target - coins[ind]]

                dp[ind][target] = taken + not_taken

        return dp[n - 1][amount]



        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # # memooization solution

        # n = len(coins)

        # def helper(ind, current_amount, coins, dp):
        #     # base case: if we have reached the first element of the array
        #     if ind == 0:
        #         return 1 if current_amount % coins[0] == 0 else 0
            
        #     if dp[ind][current_amount] != -1:
        #         return dp[ind][current_amount]

        #     not_taken = helper(ind - 1, current_amount, coins, dp)

        #     taken = 0
        #     if coins[ind] <= current_amount:
        #         taken = helper(ind, current_amount - coins[ind], coins, dp)

        #     dp[ind][current_amount] = taken + not_taken

        #     return dp[ind][current_amount]

        # dp = [[-1 for _ in range(amount + 1)] for _ in range(n + 1)]

        # return helper(n - 1, amount, coins, dp)