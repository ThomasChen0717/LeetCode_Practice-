# Approach 1: Breadth-First Search
class Solution:
    def networkDelayTime(self, times, n, k):
        adj = collections.defaultdict(list)

        for u, v, w in times:
            adj[u].append((v, w))

        q = deque([k])

        dist = [float('inf')] * (n + 1)
        dist[k] = 0

        while q:
            curr = q.popleft()

            for neighbor, weight in adj[curr]:
                if dist[curr] + weight < dist[neighbor]:
                    dist[neighbor] = dist[curr] + weight
                    q.append(neighbor)

        ans = float('-inf')
        for i in range(1, n + 1): 
            ans = max(ans, dist[i]) 
        


        return ans if ans != float('inf') else -1
        
# Approach 2: Dijkstra's Algorithm
class Solution:
    def networkDelayTime(self, times, n, k):
        adj = collections.defaultdict(list)

        for u, v, w in times:
            adj[u].append((v, w))

        heap = [(0, k)]

        dist = {}

        while heap:
            curr_time, node = heapq.heappop(heap)

            if node in dist:
                continue

            dist[node] = curr_time

            for neighbor, weight in adj[node]:
                if neighbor not in dist:
                    heapq.heappush(heap, (curr_time + weight, neighbor))

        if len(dist) != n:
            return -1

        return max(dist.values())