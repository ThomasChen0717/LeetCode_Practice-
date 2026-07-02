# Approach 1: Dijkstra's Algorithm
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])

        dis = [[-1] * n for _ in range(m)] 

        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        pq = [(grid[0][0], 0, 0)]

        while pq: 
            val, cx, cy = heapq.heappop(pq)

            if dis[cx][cy] >= 0: 
                continue 
            
            dis[cx][cy] = val 

            for dx, dy in dirs: 
                nx, ny = cx + dx, cy + dy 
                if 0 <= nx < m and 0 <= ny < n and dis[nx][ny] == -1: 
                    heapq.heappush(pq, (val + grid[nx][ny], nx, ny))
        
        return dis[m-1][n-1] < health
            
# Approach 2: 0-1 BFS
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])

        dis = [[float('inf')] * n for _ in range(m)] 

        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        q = deque() 
        q.appendleft((0,0))
        dis[0][0] = grid[0][0]

        while q: 
            cx, cy = q.popleft()

            if cx == m - 1 and cy == n - 1: 
                return True

            for dx, dy in dirs: 
                nx, ny = cx + dx, cy + dy 
                if not 0 <= nx < m or not 0 <= ny < n: 
                    continue 
                
                cost = dis[cx][cy] + grid[nx][ny] 
                if cost >= health: 
                    continue 
                
                if cost < dis[nx][ny]: 
                    dis[nx][ny] = cost 
                    if grid[nx][ny] == 1: 
                        q.append((nx, ny))
                    else: 
                        q.appendleft((nx, ny))
        
        return False
            