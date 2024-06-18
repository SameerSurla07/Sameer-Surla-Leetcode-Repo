class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums) # size of the array
        ans = []

        # sort the given array:
        nums.sort()

        # calculating the quadruplets:
        for i in range(n):
            # avoid the duplicates while moving i:
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n):
                # avoid the duplicates while moving j:
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                                # Initialize two pointers for the remaining two numbers
                k = j + 1
                l = n - 1
                while k < l:
                    _sum = nums[i] + nums[j] + nums[k] + nums[l]  # Calculate the sum of the four numbers
                    if _sum == target:
                        # If the sum matches the target, add the quadruplet to the answer list
                        temp = [nums[i], nums[j], nums[k], nums[l]]
                        ans.append(temp)
                        k += 1
                        l -= 1

                        # Skip duplicates for the third number
                        while k < l and nums[k] == nums[k - 1]:
                            k += 1
                        # Skip duplicates for the fourth number
                        while k < l and nums[l] == nums[l + 1]:
                            l -= 1
                    elif _sum < target:
                        # If the sum is less than the target, move the third pointer to the right
                        k += 1
                    else:
                        # If the sum is greater than the target, move the fourth pointer to the left
                        l -= 1

        return ans  # Return the list of quadruplets

