class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        n = len ( intervals ) # Size of the array ( list of lists )

        # Step 1: Sort the intervals based on their starting points
        intervals.sort()

        merged_intervals = []  # This will store the merged intervals

        for interval in intervals:    # Select an interval
            start, end = interval[0], interval[1]

            # Step 2: Skip all the merged intervals
            if not merged_intervals or merged_intervals[-1][1] < start:
                # Add the current interval to the merged intervals list
                merged_intervals.append([start, end])
            else:
                # There is an overlap, so merge the current interval with the previous one
                merged_intervals[-1][1] = max(merged_intervals[-1][1], end)

        return merged_intervals  # Return the list of merged intervals

