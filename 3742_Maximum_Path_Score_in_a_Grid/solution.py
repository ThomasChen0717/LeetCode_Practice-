
# Approach 1: Dynamic Programming
class Solution:
    def dfs(self, grid, i, j, k, s): 
        if i >= self.m or j >= self.n:
            return

        curr_val = grid[i][j]
        cost = self.scores[curr_val]

        if k - cost < 0:
            return

        k -= cost
        s += curr_val
        
        if i == self.m - 1 and j == self.n - 1: 
            self.max_score = max(self.max_score, s)
            return

        self.dfs(grid, i + 1, j, k, s)
        self.dfs(grid, i, j+1, k, s)


    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        self.max_score = -1
        self.scores = [0, 1, 1]
        self.m = len(grid)
        self.n = len(grid[0])

        self.dfs(grid, 0, 0, k, 0)
        return self.max_score


# Approach 2: Memoization DFS 
class Solution:
    def dfs(self, grid, i, j, k): 
        if i >= self.m or j >= self.n:
            return -1
        
        curr_val = grid[i][j]
        cost = self.scores[curr_val]

        if k - cost < 0:
            return -1

        k -= cost

        if self.memo[i][j][k] != -2:
            return self.memo[i][j][k]
        
        if i == self.m - 1 and j == self.n - 1: 
            self.memo[i][j][k] = curr_val
            return curr_val

        right = self.dfs(grid, i + 1, j, k)
        down = self.dfs(grid, i, j+1, k)

        best_next = max(down, right)

        if best_next == -1:
            self.memo[i][j][k] = -1
        else:
            self.memo[i][j][k] = curr_val + best_next

        return self.memo[i][j][k]



    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        self.scores = [0, 1, 1]
        self.m = len(grid)
        self.n = len(grid[0])
        self.memo = [[[-2] * (k + 1) for _ in range(self.n)] for _ in range(self.m)]

        return self.dfs(grid, 0, 0, k)