# Approach 1: Dynamic Programming 
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        maxarea = 0 

        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]

        for i in range(len(matrix)): 
            for j in range(len(matrix[0])): 
                if matrix[i][j] == "0": continue 

                width = dp[i][j] = dp[i][j-1] + 1 if j else 1 

                for k in range(i, -1, -1): 
                    width = min(width, dp[k][j])
                    maxarea = max(maxarea, width * (i - k + 1)) 
            
        return maxarea

# Approach 2: Stack Histogram 
class Solution:

    # Get the maximum area in a histogram given its heights
    def leetcode84(self, heights):
        stack = [-1]

        maxarea = 0
        for i in range(len(heights)):

            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                maxarea = max(
                    maxarea, heights[stack.pop()] * (i - stack[-1] - 1)
                )
            stack.append(i)

        while stack[-1] != -1:
            maxarea = max(
                maxarea, heights[stack.pop()] * (len(heights) - stack[-1] - 1)
            )
        return maxarea

    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        if not matrix:
            return 0

        maxarea = 0
        dp = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):

                # update the state of this row's histogram using the last row's histogram
                # by keeping track of the number of consecutive ones

                dp[j] = dp[j] + 1 if matrix[i][j] == "1" else 0

            # update maxarea with the maximum area from this row's histogram
            maxarea = max(maxarea, self.leetcode84(dp))
        return maxarea

# Approach 3: Dynamic Programming - Maximum Height at Each Point 

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0 

        m = len(matrix)
        n = len(matrix[0]) 

        left = [0] * n
        right = [n] * n
        height = [0] * n 

        maxarea = 0

        for i in range(m): 
            cur_left, cur_right = 0, n 

            for j in range(n): 
                if matrix[i][j] == '1': 
                    height[j] += 1
                else: 
                    height[j] = 0 
                
            for j in range(n): 
                if matrix[i][j] == '1': 
                    left[j] = max(left[j], cur_left)
                else: 
                    cur_left = j + 1
                    left[j] = 0
            
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == "1":
                    right[j] = min(right[j], cur_right)
                else:
                    right[j] = n
                    cur_right = j
            

            for j in range(n):
                maxarea = max(maxarea, height[j] * (right[j] - left[j]))
        
        return maxarea
