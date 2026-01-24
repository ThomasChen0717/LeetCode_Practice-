# Approach 1: Topological Sort with DFS
class Solution:

    WHITE = 1
    GRAY = 2
    BLACK = 3

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)

        for course, pre_req in prerequisites: 
            adj_list[pre_req].append(course)
        
        res = []

        is_possible = True 

        color = {k:self.WHITE for k in range(numCourses)} 

        def dfs(node: int): 
            nonlocal is_possible
            
            if not is_possible: return

            color[node] = self.GRAY 

            if node in adj_list: 
                for neighbor in adj_list[node]: 
                    if color[neighbor] == self.WHITE: 
                        dfs(neighbor)
                    elif color[neighbor] == self.GRAY: 
                        is_possible = False 
            
            color[node] = Solution.BLACK 
            res.append(node)

        for course in range(numCourses): 
            if color[course] == self.WHITE:
                dfs(course)
        
        return res[::-1] if is_possible else []

        
# Approach 2: Using Node Indegree
class Solution:

    WHITE = 1
    GRAY = 2
    BLACK = 3

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)

        indegree = {}

        for course, pre_req in prerequisites: 
            adj_list[pre_req].append(course)
            indegree[course] = indegree.get(course, 0) + 1
        
        res = []

        q = deque([k for k in range(numCourses) if k not in indegree])

        while q: 
            curr_course = q.popleft()
            res.append(curr_course)

            if curr_course in adj_list: 
                for neighbor in adj_list[curr_course]: 
                    indegree[neighbor] -= 1

                    if indegree[neighbor] == 0: 
                        q.append(neighbor)
            

        
        
        return res if len(res) == numCourses else []

        

        

        
