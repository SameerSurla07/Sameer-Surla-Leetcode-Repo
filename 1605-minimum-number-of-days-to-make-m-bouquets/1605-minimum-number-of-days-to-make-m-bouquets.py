class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # Optimal Approach 
        # Same helper function

        # Helper function to check if we can make required bouquets on a given day
        def canMake(bloomDay, day, m, k):
            n = len(bloomDay)
            adj = 0 # Counter for adjacent bloomed flowers
            countboq = 0 # Counter for number of bouquets formed

            for i in range(n):
                if bloomDay[i] <= day:
                    adj += 1
                    if adj == k:
                        countboq += 1
                        adj = 0
                else:
                    adj = 0

            return countboq >= m
        
        neededFlowers = m * k  # Total number of flowers needed to make m bouquets
        totalFlowers = len(bloomDay)  # Total number of flowers available

        if neededFlowers > totalFlowers:
            return -1  # Impossible case: not enough flowers to make m bouquets

        minDay = min(bloomDay)  # Minimum day any flower can bloom
        maxDay = max(bloomDay)  # Maximum day any flower can bloom
        
        # Till here was same as brute force

        # Binary search for the minimum possible day
        low, high = minDay, maxDay

        while low <= high:
            mid = (low + high) // 2  # Calculate mid point
            
            if canMake(bloomDay, mid, m, k):
                high = mid - 1  # If we can make bouquets, check earlier days
            else:
                low = mid + 1  # If we cannot make bouquets, check later days
        
        return low  # Return the minimum day found

        
        
        # Brute Force Approach ( O(2N)
        
        # # Helper function to check if we can make required bouquets on a given day
        # def canMake(bloomDay, day, m, k):
        #     n = len(bloomDay)
        #     adj = 0 # Counter for adjacent bloomed flowers
        #     countboq = 0 # Counter for number of bouquets formed

        #     for i in range(n):
        #         if bloomDay[i] <= day:
        #             adj += 1
        #             if adj == k:
        #                 countboq += 1
        #                 adj = 0
        #         else:
        #             adj = 0

        #     return countboq >= m
        
        # neededFlowers = m * k  # Total number of flowers needed to make m bouquets
        # totalFlowers = len(bloomDay)  # Total number of flowers available

        # if neededFlowers > totalFlowers:
        #     return -1  # Impossible case: not enough flowers to make m bouquets

        # minDay = min(bloomDay)  # Minimum day any flower can bloom
        # maxDay = max(bloomDay)  # Maximum day any flower can bloom

        # # Check each day from the earliest possible bloom to the latest
        # for day in range(minDay, maxDay + 1):
        #     if canMake(bloomDay, day, m, k):
        #         return day


