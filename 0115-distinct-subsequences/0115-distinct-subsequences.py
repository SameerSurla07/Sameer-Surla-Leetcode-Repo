class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        # Tabulation Approach

        n1 = len(s)
        n2 = len(t)

        dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]

        # Base case: There is exactly one subsequence of an empty string t in s1
        for i in range(n1 + 1):
            dp[i][0] = 1

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                # If current characters match
                if s[i - 1] == t[j - 1]:
                    # Include current character in both
                    include_in_both = dp[i - 1][j - 1]
                    # include in s not in t
                    include_in_s = dp[i - 1][j]

                    dp[i][j] = include_in_both + include_in_s
                else:  # If they don't match, skip 
                    dp[i][j] = dp[i - 1][j]

        return dp[n1][n2]



        
















        # # Memoized recursion
        # n1 = len(s)
        # n2 = len(t)

        # dp = [[-1 for _ in range(n2 + 1)] for _ in range(n1 + 1)]

        # def Recursive(s, t, ind1, ind2, dp):
        #     if ind2 < 0:  # We exhausted t, we found a valid subsquence
        #         return 1
        #     if ind1 < 0:  # We exhausted s, hence no valid subsequqcnce
        #         return 0  

        #     if dp[ind1][ind2] != -1:
        #         return dp[ind1][ind2]

        #     if s[ind1] == t[ind2]:
        #         leaveOne = Recursive(s, t, ind1 - 1, ind2 - 1, dp)
        #         stay = Recursive(s, t, ind1 - 1, ind2, dp)

        #         dp[ind1][ind2] = ( leaveOne + stay )

        #         return dp[ind1][ind2]

        #     else:  # If they dont match, skip from s
        #         dp[ind1][ind2] = Recursive(s, t, ind1 -1 , ind2, dp)
        #     return dp[ind1][ind2]

        # return Recursive(s, t, n1 - 1, n2 - 1, dp)















































        

        

        







