class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        m = len(customers)
        
        start_time = (customers[0][0])
        end_time = (customers[0][0] + customers[0][1])
        wait_time = (end_time - start_time)

        for i in range(1, m): 
            start_time = (max(customers[i][0] , end_time ))
            end_time = (start_time + customers[i][1]) 
            wait_time += (end_time - customers[i][0])
        
        return wait_time / len(customers)
        