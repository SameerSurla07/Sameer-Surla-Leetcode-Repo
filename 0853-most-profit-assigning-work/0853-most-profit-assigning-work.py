class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # Combine difficulty and profit into a list of tuples and sort by difficulty
        jobs = sorted(zip(difficulty, profit))
        
        # Sort workers by their abilities
        worker.sort()
        
        max_profit = 0
        best_profit = 0
        job_index = 0

        for ability in worker:
            # While there are jobs that the current worker can do
            while job_index < len(jobs) and jobs[job_index][0] <= ability:
                # Update the best_profit to the maximum profit available for the current difficulty
                best_profit = max(best_profit, jobs[job_index][1])
                job_index += 1
            # Add the best profit this worker can get to the total max_profit
            max_profit += best_profit
    
        return max_profit

