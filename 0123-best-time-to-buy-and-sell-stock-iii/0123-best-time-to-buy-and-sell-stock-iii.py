class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Intuitive short cut method

        # Initialize variables to store the "best" profits
        first_buy = float('inf')   # Initially, the first buy price is the highest possible
        first_sell = 0             # No profit initially
        second_buy = float('inf')  # Same for second buy
        second_sell = 0            # No profit initially

        for price in prices:
            # Update first buy: minimum price seen so far
            first_buy = min(first_buy, price)

            # Update first sell: maximum profit by selling at the current price after buying at first_buy
            first_sell = max(first_sell, price - first_buy)

            # Update second buy: minimum effective price after considering the profit from the first transaction
            second_buy = min(second_buy, price - first_sell)

            # Update second sell: maximum profit by selling at the current price after the second buy
            second_sell = max(second_sell, price - second_buy)

        # The answer is the maximum profit after two transactions (second sell)
        return second_sell

        
        


        # # Space optimized Approach

        # n = len(prices)
        

        # # Two variables to store the next day's results
        # # [transactions_left][canBuy]
        # next_day = [[0, 0] for _ in range(3)]
        # curr_day = [[0, 0] for _ in range(3)]

        # for ind in range(n - 1, -1, -1):
        #     for transactions_left in range(1, 3):
        #         # Calculate the maximum profit for both buying and selling
        #         buy = -prices[ind] + next_day[transactions_left][0]

        #         not_buy = next_day[transactions_left][1]

        #         curr_day[transactions_left][1] = max(buy, not_buy)

        #         sell = prices[ind] + next_day[transactions_left - 1][1]

        #         not_sell = next_day[transactions_left][0]

        #         curr_day[transactions_left][0] = max(sell, not_sell)
                    
        #     next_day = [row[:] for row in curr_day]

        # return next_day[2][1]


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # # Tabulation Approach

        # n = len(prices)

        # # dp[ind][transactions_left][canBuy]

        # dp = [[[0 for _ in range(2)] for _ in range(3)] for _ in range(n + 1)]

        # # Fill the dp table iteratively
        # for ind in range(n - 1, -1, -1):
        #     for transactions_left in range(1, 3):
        #         for canBuy in range(2):
        #             if canBuy:

        #                 buy = -prices[ind] + dp[ind + 1][transactions_left][0]

        #                 not_buy = dp[ind + 1][transactions_left][1]

        #                 dp[ind][transactions_left][1] = max(buy, not_buy)

        #             else:

        #                 sell = prices[ind] + dp[ind + 1][transactions_left - 1][1]

        #                 not_sell = dp[ind + 1][transactions_left][0]

        #                 dp[ind][transactions_left][0] = max(sell, not_sell)

        # return dp[0][2][1]



        
        
        
        
        
        
        
        
        
        
        
        
        # # Memoization Approach

        # n = len(prices)

        # # Dp table - dp[ind][transactions_left][canBuy]

        # dp = [[[-1 for _ in range(2)] for _ in range(3)] for _ in range(n)]

        # def Recursive(ind, transactions_left, canBuy):

        #     if ind == n or transactions_left == 0:
        #         return 0

        #     if dp[ind][transactions_left][canBuy] != -1:
        #         return dp[ind][transactions_left][canBuy]

        #     if canBuy:
        #         buy = -prices[ind] + Recursive(ind + 1, transactions_left, 0)

        #         dont_buy = Recursive(ind + 1, transactions_left, 1)
            
        #         dp[ind][transactions_left][canBuy] = max(buy, dont_buy)

        #     else:
        #         sell = prices[ind] + Recursive(ind + 1, transactions_left - 1, 1)

        #         dont_sell = Recursive(ind + 1, transactions_left, 0)

        #         dp[ind][transactions_left][canBuy] = max(sell, dont_sell)

        #     return dp[ind][transactions_left][canBuy]

        # return Recursive(0, 2, 1)
