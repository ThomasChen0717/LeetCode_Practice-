# Approach 1: Plain DFS 
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid) 
        m = len(obstacleGrid[0])
        def dfs(i, j): 
            if i >= n or j >= m or obstacleGrid[i][j] == 1: 
                return 0

            if i == n - 1 and j == m - 1: 
                return 1 
            
            return dfs(i+1, j) + dfs(i, j+1)

        return dfs(0,0)
                
# Approach 2: Memoization
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid) 
        m = len(obstacleGrid[0])
        memo = [[-1] * m for _ in range(n)] 

        def dfs(i, j): 
            if i >= n or j >= m or obstacleGrid[i][j] == 1: 
                return 0

            if i == n - 1 and j == m - 1: 
                return 1 

            if memo[i][j] != -1:  return memo[i][j]

            memo[i][j] = dfs(i+1, j) + dfs(i, j+1)
            
            return memo[i][j]

        return dfs(0,0)

# Approach 3: Bottom-Up DP
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid) 
        m = len(obstacleGrid[0])
        dp = [[0] * m for _ in range(n)] 

        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0

        for i in range(n): 
            for j in range(m): 
                if obstacleGrid[i][j] == 1: 
                    dp[i][j] = 0
                else: 
                    if i > 0: 
                        dp[i][j] += dp[i-1][j]
                    if j > 0: 
                        dp[i][j] += dp[i][j-1]

        return dp[n-1][m-1]

# Approach 4: DP without extra space
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid) 
        m = len(obstacleGrid[0])

        obstacleGrid[0][0] = 1 if obstacleGrid[0][0] == 0 else 0

        for i in range(n): 
            for j in range(m): 
                if obstacleGrid[i][j] == 1: 
                    obstacleGrid[i][j] = 0
                else: 
                    if i > 0: 
                        obstacleGrid[i][j] += obstacleGrid[i-1][j]
                    if j > 0: 
                        obstacleGrid[i][j] += obstacleGrid[i][j-1]

        return obstacleGrid[n-1][m-1]