# Approach 1: BFS
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()

        fresh_oranges = 0 
        r, c = len(grid), len(grid[0])

        for i in range(r):
            for j in range(c): 
                if grid[i][j] == 2: 
                    q.append((i, j))
                elif grid[i][j] == 1: 
                    fresh_oranges += 1

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        time = 0
        while q: 
            size = len(q)
            for _ in range(size): 
                row, col = q.popleft()

                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc 
                    if nr >= 0 and nr < r and nc >= 0 and nc < c and grid[nr][nc] == 1: 
                        grid[nr][nc] = 2 
                        fresh_oranges -= 1
                        q.append((nr, nc)) 

            if q: time += 1

        return time if fresh_oranges == 0 else -1 





# Approach 2: Constant Space at cost of time
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def rot(timestamp): 
            to_be_continued = False 
            for i in range(r):
                for j in range(c): 
                    if grid[i][j] == timestamp: 
                        for dr, dc in directions:
                            nr = i + dr
                            nc = j + dc 
                            if nr >= 0 and nr < r and nc >= 0 and nc < c and grid[nr][nc] == 1: 
                                grid[nr][nc] = timestamp + 1 
                                to_be_continued = True
            return to_be_continued

        timestamp = 2 
        while rot(timestamp): 
            timestamp += 1
        
        for i in range(r):
            for j in range(c): 
                if grid[i][j] == 1: return -1

        return timestamp - 2



