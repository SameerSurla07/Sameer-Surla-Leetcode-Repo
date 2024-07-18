#User function Template for python3
class Solution:

	def rowWithMax1s(self,arr):
		# code here
        cnt_max = 0
        index = -1
    
        # traverse the matrix:
        for i in range(len(arr)):
            cnt_ones = sum(arr[i])
            if cnt_ones > cnt_max:
                cnt_max = cnt_ones
                index = i
        return index

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = list(map(int, input().strip().split()))

        inputLine = list(map(int, input().strip().split()))
        arr = [[0 for j in range(m)] for i in range(n)]

        for i in range(n):
            for j in range(m):
                arr[i][j] = inputLine[i * m + j]
        ob = Solution()
        ans = ob.rowWithMax1s(arr)
        print(ans)
        tc -= 1

# } Driver Code Ends