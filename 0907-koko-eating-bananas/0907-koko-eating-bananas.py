class Solution:    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # Helper function to calculate total hours needed at speed k
        def calculateTotalHours(piles, k):
            totalHours = 0
            for pile in piles:
                totalHours += math.ceil(pile / k)
            return totalHours

        low = 0
        high = max(piles) - 1

        while low <= high :
            mid = ( low + high ) // 2

            if mid == 0:
                # Avoid division by zero
                low = mid + 1
                continue

            if calculateTotalHours(piles, mid) <= h:
                high = mid - 1

            else:
                low = mid + 1
            
        return low





        #  Brute Force approach - Linear Search
        
        # n = len(piles)
        # maxi = max(piles)

        # # Function to calculate the total hours needed at speed k
        # def calculateTotalHours(piles, k):
        #     totalH = 0
        #     for pile in piles:
        #         totalH += math.ceil(pile / k)
        #     return totalH

        # # Finding the minimum value of k using a linear search from 1 to maxi
        # for k in range(1, maxi + 1):
        #     reqTime = calculateTotalHours(piles, k)
        #     if reqTime <= h:
        #         return k

       

    


