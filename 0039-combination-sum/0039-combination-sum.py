class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        # Approach 1: Recursion

        result = []

        def backtrack(remaining, comb, start):
            # If remaining sum is 0. we found a valid combination
            if remaining == 0:
                result.append(list(comb))
                return 

            # If remaining sum is negative, stop further exploration
            if remaining < 0:
                return

            # Explore further combinations starting from current element
            for i in range(start, len(candidates)):
                comb.append(candidates[i])
                
                # Sice we can resue the same elemen, we pass 'i' instead of 'i + 1
                backtrack(remaining - candidates[i], comb, i)

                # Backtrack by removing last element
                comb.pop()

        backtrack(target, [], 0)

        return result











