# Approach 1: Brute Force Graph 
class Solution:
    def overlap(self, a, b): 
        return a[0] <= b[1] and b[0] <= a[1]

    def build_adj_list(self, intervals:List[List[int]]) -> dict: 
        graph = collections.defaultdict(list) 

        for i in range(len(intervals)): 
            for j in range(i + 1, len(intervals)): 
                if self.overlap(intervals[i], intervals[j]): 
                    graph[tuple(intervals[i])].append(intervals[j])
                    graph[tuple(intervals[j])].append(intervals[i])

        return graph
    
    def get_comps(self, graph, intervals): 
        visited = set() 
        comp_number = 0 
        nodes_in_comp = collections.defaultdict(list) 

        def dfs(node): 
            stack = [node] 
            while stack: 
                curr = tuple(stack.pop()) 
                if curr not in visited: 
                    visited.add(curr)
                    nodes_in_comp[comp_number].append(curr) 
                    stack.extend(graph[curr]) 
        
        for interval in intervals: 
            if tuple(interval) not in visited: 
                dfs(interval) 
                comp_number += 1
        
        return nodes_in_comp, comp_number

    def merge_nodes(self, nodes): 
        min_range = min(node[0] for node in nodes) 
        max_range = max(node[1] for node in nodes) 

        return [min_range, max_range]


    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        graph = self.build_adj_list(intervals) 
        components, num_comps = self.get_comps(graph, intervals) 

        return [self.merge_nodes(components[comp_num]) for comp_num in range(num_comps)]

## Approach 2: Sorting
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])

        merged = []

        for interval in intervals: 
            if not merged or merged[-1][1] < interval[0]: 
                merged.append(interval) 
            else: 
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged
