class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        # Approach 3: Tabulation Approach

        # Initialize the DP array to store teh list of combinations for each sum
        dp = [[] for _ in range(target + 1)]

        dp[0] = [[]]  # There is one way to make 0 , by taking no elements

        for candidate in candidates:
            for t in range(candidate, target + 1):
                for comb in dp[t - candidate]:
                    dp[t].append(comb + [candidate])

        return dp[target]






    # # Approach 2: Memoization ( Top-Down DP )

    #     memo = {}

    #     def backtrack(remaining, start):
    #         # If remaining sum is 0, we found a valid combination
    #         if remaining == 0:
    #             return [[]]

    #         # If remaining sum is negative, return empty list
    #         if remaining < 0:
    #             return []

    #         # Memoiation : return result is alredy computed for this state
    #         if (remaining, start) in memo:
    #             return memo[(remaining, start)]

    #         combinations = []

    #         # Explore combinations starting from current element
    #         for i in range(start, len(candidates)):
    #             new_combs = backtrack(remaining - candidates[i], i)
    #             for comb in new_combs:
    #                 combinations.append([candidates[i]] + comb)

    #         memo[(remaining, start)] = combinations
    #         return combinations

    #     return backtrack(target, 0)

        # TC : O(T x N) - T is target and N is number of candidates
        # SC - O(T x N) for memo table













    #     # Approach 1: Recursion

    #     result = []

    #     def backtrack(remaining, comb, start):
    #         # If remaining sum is 0. we found a valid combination
    #         if remaining == 0:
    #             result.append(list(comb))
    #             return 

    #         # If remaining sum is negative, stop further exploration
    #         if remaining < 0:
    #             return

    #         # Explore further combinations starting from current element
    #         for i in range(start, len(candidates)):
    #             comb.append(candidates[i])
                
    #             # Sice we can resue the same elemen, we pass 'i' instead of 'i + 1
    #             backtrack(remaining - candidates[i], comb, i)

    #             # Backtrack by removing last element
    #             comb.pop()

    #     backtrack(target, [], 0)

    #     return result

    # # TC - O(2^T) - T is target
    # # SC - O(T) - for recursion stack


   









