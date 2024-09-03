import heapq

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # Sort courses based on their last day
        courses.sort(key = lambda x: x[1])

        # max_heap to store durations of the courses we've taken so far
        max_heap = []

        current_time = 0

        for duration, lastDay in courses:
            # If we can take the course within its last day
            if current_time + duration <= lastDay:
                heapq.heappush(max_heap, -duration)
                current_time += duration
            
            # If it does exceed, replace the longest course taken so far if this one is shorter
            elif max_heap and -max_heap[0] > duration:
                current_time += duration + heapq.heappop(max_heap)  # This + heapqheappop is negative ( as it's max negative value in the heap so far), so it will get subtracted from current_time while adding
                heapq.heappush(max_heap, -duration)
            
        return len(max_heap)

