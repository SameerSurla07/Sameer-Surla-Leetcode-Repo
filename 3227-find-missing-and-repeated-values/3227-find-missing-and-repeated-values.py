class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        size = n * n
        frequency = [0] * (size + 1)

        #  Step 1 : Flatten the grid and count the occurrences
        for row in grid :
            for num in row :
                frequency[num] += 1

        #  Step 2 : Find the repeated and missing numbers
        repeating = -1
        missing = -1
        for num in range(1, size + 1):
            if frequency[num] == 2:
                repeating = num
            elif frequency[num] == 0:
                missing = num

        return [repeating, missing]