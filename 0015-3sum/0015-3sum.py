class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        #  Optimal Approach ( two pointer approach )

        # Initialize an empty list to store the unique triplets
        ans = []
        # Sort the array to handle duplicates and use two-pointer technique
        nums.sort()
        n = len(nums)

        # Iterate through the array
        for i in range(n):
            # Skip the same element to avoid duplicate triplets
            if i != 0 and nums[i] == nums[i - 1]:
                continue

            # Two pointers initialization
            j, k = i+1, n-1

            # Two-pointer technique to find the other two elements
            while j < k:
                total_sum = nums[i] + nums[j] + nums[k]
                # If the sum is less than zero, we need a larger value, move `j`
                if total_sum < 0:
                    j += 1 
                # If the sum is greater than zero, we need a smaller value, move `k`
                elif total_sum > 0:
                    k -= 1
                # If the sum is zero, we found a triplet
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    # Skip duplicates for the second pointer
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    # Skip duplicates for the third pointer
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
        return ans



        
        # # Better Approach ( Using Hashset and c = -a + -b logic)

        # # Initialize an empty set to store unique triplets
        # result = set()
        # n = len(nums)

        # # Check all possible triplets using two nested loops
        # for i in range(n):
        #     # Initialize a hash set to store elements between indices i and j
        #     hashset = set()
        #     for j in range(i+1, n):
        #         # Calculate the required third element to complete the triplet
        #         third = - ( nums[i] + nums[j] )
        #         # Check if the third element exists in the hash set
        #         if third in hashset:
        #             # Create a sorted tuple of the triplet to ensure uniqueness
        #             triplet = tuple(sorted([nums[i], nums[j], third]))
        #             result.add(triplet)

        #         # Add the current element to the hash set for future lookups
        #         hashset.add(nums[j])

        # # Convert the set of tuples to a list of lists for the expected output format
        # return [list(triplet) for triplet in result]


        
        # Brute Force Approach using 3 for loops and checking for each triplet
        
        # # Initialize an empty set to store unique triplets
        # result = set()
        # n = len(nums)

        # # Check all possible triplets using three nested loops
        # for i in range(n):
        #     for j in range(i+1, n):
        #         for k in range( j+1, n):
        #             # Check if the sum of the triplet is zero
        #             if nums[i] + nums[j] + nums[k] == 0 :
        #                 # Create a sorted tuple of the triplet to ensure uniqueness
        #                 triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
        #                 result.add(triplet)

        # # Convert set of tuples to list of lists for expected output format
        # return [list(triplet) for triplet in result]