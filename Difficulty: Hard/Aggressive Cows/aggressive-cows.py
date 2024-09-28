#User function Template for python3

class Solution:
    def solve(self,n,k,stalls):
        
        def canweplace(stalls, dist, target_cows):
            n = len(stalls)
            count_cows = 1  # number of cows placed
            last_placed = stalls[0]  # position of the last placed cow
            for i in range(1, n):
                if stalls[i] - last_placed >= dist:
                    count_cows += 1  # place next ball
                    last_placed = stalls[i]  # update the last location
                if count_cows >= target_cows:
                    return True
            return False

        n = len(stalls)
        stalls.sort()
        
        low = 1
        high = stalls[n - 1] - stalls[0]
        # apply binary search
        while low <= high:
            mid = (low + high) // 2
            if canweplace(stalls, mid, k):
                low = mid + 1
            else:
                high = mid - 1
        return high


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n, k = list(map(int, input().split()))
        stalls = list(map(int, input().split()))
        ob = Solution()
        res = ob.solve(n, k, stalls)
        print(res)

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends