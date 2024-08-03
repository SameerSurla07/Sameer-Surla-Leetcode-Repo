#User function Template for python3

class Job:
    
    # Job class which stores profit and deadline.
    
    def __init__(self,profit=0,deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0
 

class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        
        # Sort jobs by profit in descending order
        Jobs.sort(key=lambda x: x.profit, reverse=True)
        
        # Find the maximum deadline
        maxi = Jobs[0].deadline
        for i in range(1, len(Jobs)):
            maxi = max(maxi, Jobs[i].deadline)
        
        # Initialize slot array with -1 indicating empty slots
        slot = [-1] * (maxi + 1)
        countJobs = 0
        jobProfit = 0
        
        # Iterate over each job
        for i in range(len(Jobs)):
            # Try to find a slot from job's deadline to 1
            for j in range(Jobs[i].deadline, 0, -1):
                if slot[j] == -1:  # If slot is empty
                    slot[j] = i   # Schedule the job
                    countJobs += 1  # Increment job count
                    jobProfit += Jobs[i].profit  # Add profit
                    break
        
        return countJobs, jobProfit

        
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


#Contributed by : Nagendra Jha
class Job:
    '''
    Job class which stores profit and deadline.
    '''

    def __init__(self, profit=0, deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        info = list(map(int, input().strip().split()))
        Jobs = [Job() for i in range(n)]
        for i in range(n):
            Jobs[i].id = info[3 * i]
            Jobs[i].deadline = info[3 * i + 1]
            Jobs[i].profit = info[3 * i + 2]
        ob = Solution()
        res = ob.JobScheduling(Jobs, n)
        print(res[0], end=" ")
        print(res[1])

# } Driver Code Ends