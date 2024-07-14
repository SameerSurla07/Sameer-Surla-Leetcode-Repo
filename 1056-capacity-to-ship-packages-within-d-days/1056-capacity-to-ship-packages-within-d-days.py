class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def find_days(capacity):
            n = len(weights)
            num_days = 1
            weight_sum = 0
            for i in range(n):
                weight_sum += weights[i]
                if weight_sum > capacity:
                    num_days += 1
                    weight_sum = weights[i]
            return num_days

        low = max(weights)
        high = sum(weights)

        while low <= high:
            mid = ( low + high ) // 2

            if find_days(mid) > days:
                low = mid + 1
            else:
                high = mid - 1

        return low