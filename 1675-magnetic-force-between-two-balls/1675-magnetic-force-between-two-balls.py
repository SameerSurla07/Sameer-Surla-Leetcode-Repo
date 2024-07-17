class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def canweplace(position, dist, balls):
            n = len(position)
            count_balls = 1  # number of balls placed
            last = position[0]  # position of the last placed ball
            for i in range(1, n):
                if position[i] - last >= dist:
                    count_balls += 1  # place next ball
                    last = position[i]  # update the last location
                if count_balls >= balls:
                    return True
            return False

        n = len(position)
        position.sort()
        
        low = 1
        high = position[n - 1] - position[0]
        # apply binary search
        while low <= high:
            mid = (low + high) // 2
            if canweplace(position, mid, m):
                low = mid + 1
            else:
                high = mid - 1
        return high
