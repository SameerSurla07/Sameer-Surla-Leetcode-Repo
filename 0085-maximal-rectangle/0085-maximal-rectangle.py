class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def largestRectangleArea(heights):
            stack = []
            max_area = 0
            heights.append(0)  # Add a sentinel to flush out remaining heights in the stack

            for i in range(len(heights)):
                while stack and heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(i)

            heights.pop()  # Remove the sentinel
            return max_area
        if not matrix or not matrix[0]:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])
        max_area = 0

        # Initialize heights array
        heights = [0] * cols

        for i in range(rows):
            for j in range(cols):
                # Update the height of histogram
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
        
            # Compute the maximum area for the histogram represented by heights
            max_area = max(max_area, largestRectangleArea(heights))

        return max_area

