#User function Template for python3

class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, w,arr,n):
        
        # Step 1: Calculating value/weight for all items
        items = []
        for item in arr:
            ratio = item.value / item.weight
            items.append((ratio, item))
        
        # Step 2: Sort items in decreasing order
        items.sort(key=lambda x: x[0], reverse = True)
        
        # Step 3: Iterate through sorted items and fill knapsack
        total_value = 0.00
        for ratio, item in items:
            if w == 0:
                break
            if item.weight <= w:
                total_value += item.value
                w -= item.weight
            else:
                total_value += item.value * (w / item.weight)
                w = 0
            
        return total_value
                
        
        
        
        
        
        
        
        
        
        
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha


class Item:

    def __init__(self, val, w):
        self.value = val
        self.weight = w


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n, w = map(int, input().strip().split())
        info = list(map(int, input().strip().split()))
        arr = [Item(0, 0) for i in range(n)]
        for i in range(n):
            arr[i].value = info[2 * i]
            arr[i].weight = info[2 * i + 1]

        ob = Solution()
        print("%.6f" % ob.fractionalknapsack(w, arr, n))

# } Driver Code Ends