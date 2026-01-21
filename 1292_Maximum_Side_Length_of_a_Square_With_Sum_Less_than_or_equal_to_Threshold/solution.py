# Approach 1: 2D Prefix Sum + Binary Search
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        P = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1): 
            for j in range(1, n + 1): 
                P[i][j] = P[i-1][j] + P[i][j-1] - P[i-1][j-1] + mat[i-1][j-1]
        
        def get_rect_sum(x1, y1, x2, y2): 
            return P[x2][y2] - P[x2][y1 - 1] - P[x1 - 1][y2] + P[x1 - 1][y1 - 1] 
        
        lo, hi = 1, min(m, n)
        ans = 0
        while lo <= hi: 
            mid = lo + (hi - lo) // 2
            find = any(
                get_rect_sum(i, j, i + mid - 1, j + mid - 1) <= threshold
                for i in range(1, m - mid + 2)
                for j in range(1, n - mid + 2)
            )

            if find: 
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        
        return ans

# Approach 2: 2D Prefix Sum + Optimized Enumeration
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        P = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                P[i][j] = (
                    P[i - 1][j]
                    + P[i][j - 1]
                    - P[i - 1][j - 1]
                    + mat[i - 1][j - 1]
                )

        def getRect(x1, y1, x2, y2):
            return P[x2][y2] - P[x1 - 1][y2] - P[x2][y1 - 1] + P[x1 - 1][y1 - 1]

        r, ans = min(m, n), 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                for c in range(ans + 1, r + 1):
                    if (
                        i + c - 1 <= m
                        and j + c - 1 <= n
                        and getRect(i, j, i + c - 1, j + c - 1) <= threshold
                    ):
                        ans += 1
                    else:
                        break
        return ans