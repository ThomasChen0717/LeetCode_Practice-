## Approach 1: Breadth-First Search
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum, ans, level = float('-inf'), 0, 0
        curr_sum = 0

        q = collections.deque([root, None])

        while q: 
            curr = q.popleft() 
            if curr == None: 
                level += 1
                if len(q) != 0: 
                    q.append(None)
                if curr_sum > max_sum: 
                    max_sum = curr_sum 
                    ans = level
                curr_sum = 0
            else: 
                curr_sum += curr.val
                if curr.left: 
                    q.append(curr.left)
                if curr.right: 
                    q.append(curr.right)
        
        return ans

## Approach 2: Depth-First Search
class Solution:
    def dfs(self, root, level, sum_of_nodes_at_level): 
        if root is None: return 

        if len(sum_of_nodes_at_level) == level: 
            sum_of_nodes_at_level.append(root.val)
        else: 
            sum_of_nodes_at_level[level] += root.val 
        
        self.dfs(root.left, level + 1, sum_of_nodes_at_level)
        self.dfs(root.right, level + 1, sum_of_nodes_at_level)
    
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        sum_of_nodes_at_level = []
        self.dfs(root, 0, sum_of_nodes_at_level) 

        max_sum = float("-inf")
        ans = 0 

        for i in range(len(sum_of_nodes_at_level)): 
            if sum_of_nodes_at_level[i] > max_sum: 
                max_sum = sum_of_nodes_at_level[i]
                ans = i + 1
        
        return ans



