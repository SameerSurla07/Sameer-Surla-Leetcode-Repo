#User function Template for python3

class Solution:
	def NthRoot(self, n, m):
		# Code here

        low = 0
        high = m
        ans = m + 1
        
        while low <= high :
            mid = ( low + high ) // 2
            
            val = mid ** n
            
            if val == m:
                return mid
            
            if val < m :
                low = mid + 1
                
            else:
                high = mid - 1
        
        return -1
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n); m = int(m);
		ob = Solution()
		ans = ob.NthRoot(n, m)
		print(ans)
# } Driver Code Ends