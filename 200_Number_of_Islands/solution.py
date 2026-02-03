# Approach 1: DFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        def dfs(i, j):
            if i >= n or j >= m or i < 0 or j <  0 or grid[i][j] == '0': 
                return 
            
            grid[i][j] = '0' 

            dfs(i + 1, j) 
            dfs(i, j + 1)
            dfs(i - 1, j)
            dfs(i, j - 1)
        
        count = 0
        for i in range(n): 
            for j in range(m): 
                if grid[i][j] == '1': 
                    dfs(i, j)
                    count += 1

        return count

# Approach 2: BFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        nr = len(grid)
        nc = len(grid[0])
        num_islands = 0

        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    num_islands += 1
                    grid[r][c] = "0"  # mark as visited
                    neighbors = []
                    neighbors.append((r, c))
                    while neighbors:
                        row, col = neighbors.pop(0)
                        if row - 1 >= 0 and grid[row - 1][col] == "1":
                            neighbors.append((row - 1, col))
                            grid[row - 1][col] = "0"
                        if row + 1 < nr and grid[row + 1][col] == "1":
                            neighbors.append((row + 1, col))
                            grid[row + 1][col] = "0"
                        if col - 1 >= 0 and grid[row][col - 1] == "1":
                            neighbors.append((row, col - 1))
                            grid[row][col - 1] = "0"
                        if col + 1 < nc and grid[row][col + 1] == "1":
                            neighbors.append((row, col + 1))
                            grid[row][col + 1] = "0"
        return num_islands

# Approach 3: Union Find
class UnionFind:
    def __init__(self, grid):
        self.count = 0
        m, n = len(grid), len(grid[0])
        self.parent = []
        self.rank = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.parent.append(i * n + j)
                    self.count += 1
                else:
                    self.parent.append(-1)
                self.rank.append(0)

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.parent[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.parent[rootx] = rooty
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1
            self.count -= 1

    def getCount(self):
        return self.count


class Solution:
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0

        nr = len(grid)
        nc = len(grid[0])
        uf = UnionFind(grid)

        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    grid[r][c] = "0"
                    if r - 1 >= 0 and grid[r - 1][c] == "1":
                        uf.union(r * nc + c, (r - 1) * nc + c)
                    if r + 1 < nr and grid[r + 1][c] == "1":
                        uf.union(r * nc + c, (r + 1) * nc + c)
                    if c - 1 >= 0 and grid[r][c - 1] == "1":
                        uf.union(r * nc + c, r * nc + c - 1)
                    if c + 1 < nc and grid[r][c + 1] == "1":
                        uf.union(r * nc + c, r * nc + c + 1)

        return uf.getCount()