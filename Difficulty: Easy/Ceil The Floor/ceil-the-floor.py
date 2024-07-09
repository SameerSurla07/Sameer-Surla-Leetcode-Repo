#User function Template for python3
def getFloorAndCeil(arr, n, x):
    # code here
    # Initialize floor and ceil values
    floor_val = -1
    ceil_val = 1000001
    
    # Traverse the array
    for num in arr:
        if num <= x and num > floor_val:
            floor_val = num
        if num >= x and num < ceil_val:
            ceil_val = num
            
    # If no ceil value found, set it to -1
    if ceil_val == 1000001:
        ceil_val = -1
        
    return (floor_val, ceil_val)
            
#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))

        ans = getFloorAndCeil(arr, n, x)
        print(str(ans[0]) + " " + str(ans[1]))
        tc -= 1

# } Driver Code Ends