#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here
        # Combine start and end times into a list of tuples
        meetings = list(zip(start, end))
        
        # Sort meetings based on end times
        meetings.sort(key=lambda x: x[1])

        # Initialize count of meetings and the end time of the last meeting
        count = 0
        last_end_time = 0

        # Iterate over the sorted meetings
        for s, e in meetings:
            if s > last_end_time:
                # If the start time of the current meeting is greater than
                # the end time of the last meeting, select this meeting
                count += 1
                last_end_time = e
        
        return count

        
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maximumMeetings(n,start,end))
# } Driver Code Ends