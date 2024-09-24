#User function Template for python3

class Solution:
    def cutRod(self, price, n):
        #code here

        
        # Create a DP array to store the maximum profit for each length of rod
        dp = [0] * (n + 1)  # dp[i] will store the maximum profit for rod of length i
        
        # Iterate through all lengths from 1 to n
        for i in range(1, n + 1):
            # For each length, try cutting at every possible position (from 1 to i)
            for j in range(1, i + 1):
                dp[i] = max(dp[i], price[j - 1] + dp[i - j])
        
        # The value dp[n] will have the maximum profit for rod of length n
        return dp[n]

            
            
            
            
            
            
            
            
                
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.cutRod(a, n))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends