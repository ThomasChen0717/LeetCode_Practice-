# Approach 1: Binary Search + Dijkstra's Algorithm
class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:

        n = len(online) 
        adj = [[] for _ in range(n)] 
        l, r = float("inf"), 0 

        for u, v, w in edges: 
            if not online[u] or not online[v]: 
                continue 
            adj[u].append((v, w))
            l = min(l, w)
            r = max(r, w)
        
        if l == float("inf") or not online[0] or not online[n-1]:
            return -1
        
        def check(mid: int) -> bool: 
            pq = [(0,0)]
            dis = [float("inf")] * n
            dis[0] = 0

            while pq: 
                dist, node = heapq.heappop(pq) 

                if dist > k: 
                    return False 
                if node == n - 1: 
                    return True 
                if dist > dis[node]: 
                    continue 
                
                for neighbor, cost in adj[node]: 
                    if cost < mid: continue 
                    if dis[neighbor] > dis[node] + cost: 
                        dis[neighbor] = dis[node] + cost 
                        heapq.heappush(pq, (dis[neighbor], neighbor))
                
            return False
        
        if not check(l): 
            return -1

        while l <= r: 
            mid = r - (r - l) // 2
            if check(mid): 
                l = mid + 1
            else: 
                r = mid - 1
        
        return r

# Approach 2: Binary Search + Memoization DFS
class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:

        n = len(online) 
        adj = [[] for _ in range(n)] 
        l, r = float("inf"), 0 

        for u, v, w in edges: 
            if not online[u] or not online[v]: 
                continue 
            adj[u].append((v, w))
            l = min(l, w)
            r = max(r, w)
        
        if l == float("inf") or not online[0] or not online[n-1]:
            return -1
        
        def check(mid: int) -> bool: 
            memo = [-1] * n 

            def dfs(node: int) -> int: 
                if node == n - 1: return 0
                if memo[node] != -1: return memo[node]
                
                res = float('inf')
                for v, w in adj[node]: 
                    if w >= mid: 
                        res = min(res, dfs(v) + w)
                
                memo[node] = res
                return res
            
            return dfs(0) <= k
        
        if not check(l): 
            return -1

        while l <= r: 
            mid = r - (r - l) // 2
            if check(mid): 
                l = mid + 1
            else: 
                r = mid - 1
        
        return r

# Approach 3: Binary Search + Topological DP
class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        g = [[] for _ in range(n)]
        deg = [0] * n
        l, r = float('inf'), 0

        for u, v, w in edges:
            if not online[u] or not online[v]:
                continue
            g[u].append((v, w))
            deg[v] += 1
            l = min(l, w)
            r = max(r, w)

        # 删除不可达节点
        q = deque([i for i in range(1, n) if deg[i] == 0])
        while q:
            u = q.popleft()
            for v, _ in g[u]:
                deg[v] -= 1
                if v and deg[v] == 0:
                    q.append(v)

        def check(mid: int) -> bool:
            dp = [math.inf] * n
            cdeg = deg.copy()
            dp[0] = 0
            
            q = deque([0])
            while q:
                u = q.popleft()
                if u == n - 1:
                    return dp[u] <= k
                
                for v, w in g[u]:
                    if w >= mid:
                        dp[v] = min(dp[v], dp[u] + w)
                    cdeg[v] -= 1
                    if cdeg[v] == 0:
                        q.append(v)
            return False

        if not check(l):
            return -1

        while l <= r:
            mid = (l + r) >> 1
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1
        
        return r