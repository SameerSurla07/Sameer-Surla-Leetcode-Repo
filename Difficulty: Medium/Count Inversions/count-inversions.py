from typing import List

class Solution:
    def merge(self, arr: List[int], temp_arr: List[int], left: int, mid: int, right: int) -> int:
        i = left    # Starting index for left subarray
        j = mid + 1 # Starting index for right subarray
        k = left    # Starting index to be sorted
        inv_count = 0
  
        # Conditions are checked to ensure that i doesn't exceed mid and j doesn't exceed right
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp_arr[k] = arr[i]
                i += 1
            else:
                temp_arr[k] = arr[j]
                inv_count += (mid-i + 1)
                j += 1
            k += 1
  
        # Copy the remaining elements of left subarray, if any
        while i <= mid:
            temp_arr[k] = arr[i]
            i += 1
            k += 1
  
        # Copy the remaining elements of right subarray, if any
        while j <= right:
            temp_arr[k] = arr[j]
            j += 1
            k += 1
  
        # Copy the sorted subarray into Original array
        for i in range(left, right + 1):
            arr[i] = temp_arr[i]
          
        return inv_count
  
    def mergeSort(self, arr: List[int], temp_arr: List[int], left: int, right: int) -> int:
        inv_count = 0
        if left < right:
            mid = (left + right) // 2
  
            inv_count += self.mergeSort(arr, temp_arr, left, mid)
            inv_count += self.mergeSort(arr, temp_arr, mid + 1, right)
            inv_count += self.merge(arr, temp_arr, left, mid, right)
  
        return inv_count
  
    def inversionCount(self, arr: List[int], n: int) -> int:
        temp_arr = [0] * n
        return self.mergeSort(arr, temp_arr, 0, n - 1)


        # Your Code Here
        # count = 0
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if arr[i] > arr[j]:
        #             count += 1
        # return count
                
            
     
                
                
                
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a, n))

# } Driver Code Ends