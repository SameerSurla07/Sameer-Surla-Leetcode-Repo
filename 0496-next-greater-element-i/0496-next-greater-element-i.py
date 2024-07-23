class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Dictionary to hold the next greater element for each number in nums2
        next_greater = {}
        # Stack to keep track of elements for which we are trying to find the next greater element
        stack = []

        # Iterate through each element in nums2
        for num in nums2:
            # If stack is not empty and current number is greater than the top element in the stack
            while stack and num > stack[-1]:
                # Pop the top element from the stack and set its next greater element in the dictionary
                next_greater[stack.pop()] = num
            # Push the current number onto the stack
            stack.append(num)

        # For elements left in the stack, there is no next greater element, so set it to -1
        while stack:
            next_greater[stack.pop()] = -1

        # Prepare the result for nums1 by mapping each element to its next greater element using the dictionary
        return [next_greater[num] for num in nums1]
        
        # # Helper function to find the next greater element for x in arr
        # def findgreater(arr, x):
        #     found = False
        #     for i in range(len(arr)):
        #         # Check if the current element is the one we're looking for
        #         if arr[i] == x:
        #             found = True
        #         # If we have found x, check for the next greater element
        #         if found and arr[i] > x:
        #             return arr[i]
        #     # If no greater element is found, return -1
        #     return -1
        
        # ans = []  # List to store the results

        # # Iterate over each element in nums1
        # for num in nums1:
        #     # Find the next greater element for each num in nums1
        #     ans.append(findgreater(nums2, num))
        
        # return ans
