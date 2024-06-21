class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # Optimal Solution
        # Step 1: Sort the intervals based on their starting points
        intervals.sort(key=lambda x: x[0])
        
        merged_intervals = []  # This will store the merged intervals

        for interval in intervals:
            # If merged_intervals is empty or the current interval does not overlap with the last merged interval
            if not merged_intervals or merged_intervals[-1][1] < interval[0]:
                # Add the current interval as it does not overlap with the last one
                merged_intervals.append(interval)
            else:
                # Merge the current interval with the last interval in merged_intervals
                # by updating the end time to the maximum end time of the two overlapping intervals
                merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])

        return merged_intervals  # Return the list of merged intervals

        
        # Brute force solution

        # n = len ( intervals ) # Size of the array ( list of lists )

        # # Step 1: Sort the intervals based on their starting points
        # intervals.sort()

        # merged_intervals = []  # This will store the merged intervals

        # for interval in intervals:    # Select an interval
        #     start, end = interval[0], interval[1]

        #     # Step 2: Skip all the merged intervals
        #     if not merged_intervals or merged_intervals[-1][1] < start:
        #         # Add the current interval to the merged intervals list
        #         merged_intervals.append([start, end])
        #     else:
        #         # There is an overlap, so merge the current interval with the previous one
        #         merged_intervals[-1][1] = max(merged_intervals[-1][1], end)

        # return merged_intervals  # Return the list of merged intervals

