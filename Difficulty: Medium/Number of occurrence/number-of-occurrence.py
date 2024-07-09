#User function Template for python3
class Solution:

	def count(self,arr, n, x):
		# code here
        low = 0
        high = n -1
        first, last = -1, -1
        
        while low <= high :
            mid = ( low + high ) // 2
            if arr[mid] > x :
                high = mid - 1
            
            elif arr[mid] == x:
                first = mid
                high = mid - 1
                
            else:
                low = mid + 1
        
        
        
        low = 0
        high = n-1
        
        while low <= high :
            mid = ( low + high ) // 2
            if arr[mid] <= x :
                last = mid
                low = mid + 1
                
            else:
                 high = mid - 1
        
        
        
        if first == -1:
            return 0
            
        return last - first + 1
            
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.count(arr, n, x)
        print(ans)
        tc -= 1

# } Driver Code Ends