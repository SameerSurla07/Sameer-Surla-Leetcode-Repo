#User function Template for python3

class Solution:
    def minimumEnergy(self, height, n):
        # Code here

        # Base case: If only 1 stair, 0 energy required
        if n == 1:
            return 0
        
        # Create a dp array to store minimum energy
        # required to reach each stair
        dp = [0] * n
        
        # Energy required to reach the first stair is always 0
        dp[0] = 0
        
        # Minimum energy required for 1st stair
        dp[1] = abs(height[1] - height[0])
        
        # Iterate over the rest of the stairs and calculate the minimum energy
        for i in range(2, n):
            # Energy to jump to (i-1)th stair
            jump_one = dp[i-1] + abs(height[i] - height[i-1])
            # Energy to jump to (i-2)th stair
            jump_two = dp[i-2] + abs(height[i] - height[i-2])
            # Take the minimum of the two possible jumps
            dp[i] = min(jump_one, jump_two)
            
        
        return dp[n-1]

            
            








#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        height = list(map(int, input().split()))
        ob = Solution()
        print(ob.minimumEnergy(height, n))
# } Driver Code Ends