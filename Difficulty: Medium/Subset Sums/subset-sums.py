#User function Template for python3
class Solution:
	def subsetSums(self, arr, n):
		# code here
		def generate(index, current_sum):
		    # Base case: If we have considered all elements
		    if index == n:
		        result.append(current_sum)
		        return
		    
		    # Recursive case 1: Exclude the current element and move on to the next
		    generate(index + 1, current_sum)
		    
		    # Recursive case 2: Include the current element in the sum and move to the next
		    generate(index + 1, current_sum + arr[index])
		    
# 		Initialize result list to store all subset sums
        result = []
        
        generate(0,0)
        
        return result
                
                
                
                
                
                
                
                
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x, end=" ")
        print("")

# } Driver Code Ends