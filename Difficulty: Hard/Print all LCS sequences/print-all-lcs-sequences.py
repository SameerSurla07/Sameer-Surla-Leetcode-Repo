#User function Template for python3

class Solution:
	def all_longest_common_subsequences(self, s1, s2):
		# Code here
       
        
        n,m = len(s1),len(s2)
        dp = [[-1 for _ in range(m+1)] for _ in range(n+1)]
        for i2 in range(m+1):
            dp[0][i2] = 0
        for i1 in range(n+1):
            dp[i1][0] = 0
        for i1 in range(1,n+1):
            for i2 in range(1,m+1):
                if s1[i1-1]==s2[i2-1]:
                    dp[i1][i2] = 1 + dp[i1-1][i2-1]
                else:
                    dp[i1][i2] = max(dp[i1-1][i2],dp[i1][i2-1])
        memo = {}
        
        # Step 2: Backtracking with memoization to collect all LCSs
        def backtrack(i, j):
            if i == 0 or j == 0:
                return {""}
            if (i, j) in memo:
                return memo[(i, j)]
            
            if s1[i - 1] == s2[j - 1]:
                subsequences = backtrack(i - 1, j - 1)
                result = {subseq + s1[i - 1] for subseq in subsequences}
            else:
                subsequences = set()
                if dp[i - 1][j] == dp[i][j]:
                    subsequences.update(backtrack(i - 1, j))
                if dp[i][j - 1] == dp[i][j]:
                    subsequences.update(backtrack(i, j - 1))
                result = subsequences
            
            memo[(i, j)] = result
            return result
        
        # Step 3: Generate all LCS and sort them lexicographically
        lcs_set = backtrack(n, m)
        return sorted(lcs_set)
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # # Tabulation with backtracking
        
        # # Step 1: length of strings
        
        # n1 = len(s)
        # n2 = len(t)
        
        # # Step 2: create a DP table intitialized with 0
        # dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]
        
        # # Step 3: Fill the DP table iteratively
        # for i in range(1, n1 + 1):
        #     for j in range(1, n2 + 1):
        #         if s[i - 1] == t[j - 1]:
        #             dp[i][j] = 1 + dp[i - 1][j - 1]
        #         else:
        #             dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                    
        # # Step 4: Backtrack to collect all LCS strings
        
        # def backtrack(i, j):
        #     if i == 0 or j == 0:
        #         return {""}
                
        #     if s[i - 1] == t[j - 1]:
        #         previous_subsequences = backtrack(i - 1, j - 1)
        #         subsequences = set()
        #         for sub in previous_subsequences:
        #             subsequences.add(sub + s[i - 1])  
        #         return subsequences
                    
        #     else:
        #         subsequences = set()
        #         if dp[i-1][j] == dp[i][j]:  # MOve up
        #             subsequences.update(backtrack(i - 1, j))
        #         if dp[i][j-1] == dp[i][j]:  # MOve left
        #             subsequences.update(backtrack(i, j - 1))
        #         return subsequences
                    
        # # Step 5: Collect all LCS subsequences and sort them lexicographically
        # lcs_sequences = backtrack(n1, n2)
        # return sorted(lcs_sequences)
        
        
        
        
        
        
        
        
        
        
        
        # # Memoization Approach + backtracking
        
        # # Step 1: Lengths of strings
        # n, m = len(s), len(t)
        
        # # Step 2: Create a memoization table initialized with -1
        # dp = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]

        # # Recursive function to compute LCS length using memoization
        # def lcs_length(i, j):
        #     # Base case: If either string is exhausted, LCS length is 0
        #     if i == 0 or j == 0:
        #         return 0
            
        #     # If already computed, return stored value
        #     if dp[i][j] != -1:
        #         return dp[i][j]
            
        #     # If characters match, move diagonally left and add 1 to the LCS
        #     if s[i - 1] == t[j - 1]:
        #         dp[i][j] = 1 + lcs_length(i - 1, j - 1)
        #     else:
        #         # Else, take the maximum from skipping either character
        #         dp[i][j] = max(lcs_length(i - 1, j), lcs_length(i, j - 1))
            
        #     return dp[i][j]

        # # Step 3: Get the LCS length
        # lcs_length(n, m)

        # # Step 4: Backtrack to collect all LCS strings
        # def backtrack(i, j):
        #     # Base case: If either string is exhausted, return an empty subsequence
        #     if i == 0 or j == 0:
        #         return {""}
            
        #     # If characters match, take the diagonal path in the dp table
        #     if s[i - 1] == t[j - 1]:
        #         previous_subsequences = backtrack(i - 1, j - 1)
        #         return {sub + s[i - 1] for sub in previous_subsequences}
        #     else:
        #         # Collect subsequences from both options (move up or move left)
        #         subsequences = set()
        #         if dp[i - 1][j] == dp[i][j]:  # Move up
        #             subsequences.update(backtrack(i - 1, j))
        #         if dp[i][j - 1] == dp[i][j]:  # Move left
        #             subsequences.update(backtrack(i, j - 1))
                
        #         return subsequences

        # # Step 5: Collect all LCS subsequences and sort them lexicographically
        # lcs_sequences = backtrack(n, m)
        # return sorted(lcs_sequences)


        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s, t = input().split()
        ob = Solution()
        ans = ob.all_longest_common_subsequences(s, t)
        for i in ans:
            print(i, end=" ")
        print()

# } Driver Code Ends