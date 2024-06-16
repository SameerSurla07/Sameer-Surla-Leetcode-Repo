class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        #  Better Approach ( Using Hashmap )

        n = len ( nums )   # Get the size of the array
        freq_map = defaultdict(int) # Initialize a hashmap to store frequency of element

        # Traverse the array and populate the hashmap with frequencies
        for num in nums:
            freq_map[num] += 1

        # Initialize an empty list to store the majority elemets
        result = []

        # Check the hashmap for frequencies greater than m/3
        for key, value in freq_map.items():
            if value > n//3:
                result.append(key)

        return result

        
        
        # # Brute force approach

        # n = len ( nums ) # Size of the list
        # ls = []  # List to store the majority elements
        
        # for i in range(n):
        #     # Selected element is nums [i]
        #     # Check if nums [i] is not already in the result list
        #     if len(ls) == 0 or (nums[i] != ls[0] and len(ls) > 0):
        #         cnt = 0  # Initialize count for the current element
        #         for j in range(n):
        #             # Count the frequency of nums[i]
        #             if nums [i] == nums [j]:
        #                 cnt += 1
                
        #         # Check if the frequency is greater than n/3

        #         if (cnt > n//3) :
        #             ls.append(nums[i])

        #     #  If we have found 2 majority element, break the loop
        #     if len(ls) == 2:
        #         break
        
        # return ls
