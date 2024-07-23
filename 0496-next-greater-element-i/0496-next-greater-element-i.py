class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Helper function to find the next greater element for x in arr
        def findgreater(arr, x):
            found = False
            for i in range(len(arr)):
                # Check if the current element is the one we're looking for
                if arr[i] == x:
                    found = True
                # If we have found x, check for the next greater element
                if found and arr[i] > x:
                    return arr[i]
            # If no greater element is found, return -1
            return -1
        
        ans = []  # List to store the results

        # Iterate over each element in nums1
        for num in nums1:
            # Find the next greater element for each num in nums1
            ans.append(findgreater(nums2, num))
        
        return ans

