# Approach 1: 2D Bottom-Up Dynamic Programming
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0]) 
        dp = [[0] * n for _ in range(m)]

        for i in range(m): 
            for j in range(n): 
                if i == 0 and j != 0: 
                    dp[i][j] = grid[i][j] + dp[i][j-1]
                elif j == 0  and i != 0: 
                    dp[i][j] = grid[i][j] + dp[i-1][j]
                elif i != 0 and j != 0: 
                    dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
                else: 
                    dp[i][j] = grid[i][j]
        
        return dp[m-1][n-1]

# Approach 2: 1D Bottom-Up Dynamic Programming
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0]) 
        dp = [0] * n

        for i in range(m): 
            for j in range(n): 
                if i == 0 and j != 0: 
                    dp[j] = grid[i][j] + dp[j-1]
                elif j == 0  and i != 0: 
                    dp[j] = grid[i][j] + dp[j]
                elif i != 0 and j != 0: 
                    dp[j] = grid[i][j] + min(dp[j-1], dp[j])
                else: 
                    dp[j] = grid[i][j]
        
        return dp[n-1]

# Approach 3: Constant Space Dynamic Programming
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j != 0:
                    grid[i][j] += grid[i][j - 1]
                elif j == 0 and i != 0:
                    grid[i][j] += grid[i - 1][j]
                elif j != 0 and i != 0:
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[len(grid) - 1][len(grid[0]) - 1]