# Approach 1: Topological Sort (Kahn's Algorithm)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses

        edge_map = collections.defaultdict(list)


        q = deque()

        for target, prereq in prerequisites: 
            edge_map[prereq].append(target) 
            indegree[target] += 1

        for i in range(len(indegree)): 
            if indegree[i] == 0:
                q.append(i) 
        
        visited = 0

        while q: 
            curr = q.popleft() 
            visited += 1

            for course in edge_map[curr]: 
                indegree[course] -= 1 
                if indegree[course] == 0: 
                    q.append(course) 
            

        return visited == numCourses

# Approach 2: DFS
class Solution:
    def dfs(self, node, adj, visit, inStack):
        
        if inStack[node]:
            return True
        if visit[node]:
            return False
       
        inStack[node] = True
        for neighbor in adj[node]:
            if self.dfs(neighbor, adj, visit, inStack):
                return True
        
        inStack[node] = False
        return False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for prerequisite in prerequisites:
            adj[prerequisite[1]].append(prerequisite[0])

        visit = [False] * numCourses
        inStack = [False] * numCourses
        for i in range(numCourses):
            if self.dfs(i, adj, visit, inStack):
                return False
        return True            
