# Approach 1: Dijkstra's Algorithm
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        pq = [(grid[0][0], 0, 0)]
        seen = {(0,0)} 
        ans = 0 

        while pq: 
            d, r, c = heapq.heappop(pq)
            ans = max(d, ans)
            if r == c == n-1: return ans 

            for dr, dc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)): 
                if (dr, dc) not in seen and 0 <= dr < n and 0 <= dc < n: 
                    heapq.heappush(pq, (grid[dr][dc], dr, dc))
                    seen.add((dr, dc))
                    
    

