class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Brute force approach

        n = len ( nums ) # Size of the list
        ls = []  # List to store the majority elements
        
        for i in range(n):
            # Selected element is nums [i]
            # Check if nums [i] is not already in the result list
            if len(ls) == 0 or (nums[i] != ls[0] and len(ls) > 0):
                cnt = 0  # Initialize count for the current element
                for j in range(n):
                    # Count the frequency of nums[i]
                    if nums [i] == nums [j]:
                        cnt += 1
                
                # Check if the frequency is greater than n/3

                if (cnt > n//3) :
                    ls.append(nums[i])

            #  If we have found 2 majority element, break the loop
            if len(ls) == 2:
                break
        
        return ls
