class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1: # If there is only one person, they are the judge by default.
            return 1
        
        # Initialize in-degree and out-degree arrays
        in_degree = [0] * (n + 1)
        out_degree = [0] * (n + 1)

        # Populate the in-degree and out-degree arrays
        for a, b in trust:
            out_degree[a] += 1
            in_degree[b] += 1

        # Identify the judge
        for person in range(1, n + 1):
            if in_degree[person] == n - 1 and out_degree[person] == 0:
                return person
        
        return -1




        
