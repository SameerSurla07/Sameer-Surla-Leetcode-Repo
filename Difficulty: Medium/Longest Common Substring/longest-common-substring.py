#User function Template for python3

class Solution:
    def longestCommonSubstr(self, str1, str2):
        # code here
        
        #Tabulation Approach ( )
        
        n = len(str1)
        m = len(str2)
        ans = 0
        
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        
        for ind1 in range(1, n + 1):
            for ind2 in range(1, m + 1):
                if str1[ind1 - 1] == str2[ind2 - 1]:
                    dp[ind1][ind2] = 1 + dp[ind1 - 1][ind2 - 1]
                    ans = max(dp[ind1][ind2], ans)
                else:
                    dp[ind1][ind2] = 0
        
        return ans
        
        
        
        
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S1 = input().strip()
        S2 = input().strip()
        ob = Solution()
        print(ob.longestCommonSubstr(S1, S2))

# } Driver Code Ends