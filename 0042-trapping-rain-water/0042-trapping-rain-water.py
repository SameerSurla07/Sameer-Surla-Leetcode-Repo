class Solution:
    def trap(self, height: List[int]) -> int:
        # Optimal approach
        if not height:
            return 0

        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water_trapped = 0

        while left < right:
            if height[left] < height[right]:
                left += 1
                left_max = max(left_max, height[left])
                water_trapped += max(0, left_max - height[left])
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water_trapped += max(0, right_max - height[right])

        return water_trapped





        # # Better Approach - O(3N) 

        # n = len(height)
        # prefix = [0] * n
        # suffix = [0] * n

        # prefix[0] = height[0] 
        # suffix[n-1] = height[n-1]

        # for i in range(1,n):
        #     prefix[i] = max ( prefix[i-1], height[i])

        # for i in range(n-2, -1, -1):
        #     suffix[i] = max( suffix[i+1], height[i])

        # total = 0
        # for i in range(n):
        #     total += min( prefix[i], suffix[i] ) - height[i]

        # return total 
        
        # #Brute Force Approach 

        # n = len(height)
        # total = 0

        # for i in range(n):
        #     j = i
        #     lmax = 0
        #     rmax = 0

        #     while j >= 0:
        #         lmax = max ( lmax, height[j])
        #         j -= 1
        #     j = i

        #     while j < n:
        #         rmax = max ( rmax, height[j])
        #         j += 1
        #     j = i
        
        #     total += min(lmax, rmax) - height[i]
        
        # return total



            