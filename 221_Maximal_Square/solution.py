# Approach 1: 2D Dynamic Programming
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])

        dp = [[0] * (m+1) for _ in range(n+1)]

        max_side_len = 0

        for i in range(n): 
            for j in range(m): 
                if matrix[i][j] == '1': 
                    dp[i+1][j+1] = min(dp[i][j+1], dp[i+1][j], dp[i][j]) + 1
                    max_side_len = max(max_side_len, dp[i+1][j+1])

        return max_side_len ** 2

        
# Approach 2: 1D Dynamic Programming
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])

        dp = [0] * (m+1) 

        max_side_len = 0

        prev = 0

        for i in range(n): 
            for j in range(m): 
                tmp = dp[j+1]
                if matrix[i][j] == '1': 
                    dp[j+1] = min(dp[j+1], dp[j], prev) + 1
                    max_side_len = max(max_side_len, dp[i+1])
                else: 
                    dp[j+1] = 0
                prev = tmp

        return max_side_len ** 2

        
