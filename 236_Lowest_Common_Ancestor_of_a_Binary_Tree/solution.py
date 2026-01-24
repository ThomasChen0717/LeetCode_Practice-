# Approach 1: DFS Recursive

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None 

        def dfs(node): 
            nonlocal ans
            if not node: return False 

            left = dfs(node.left)
            right = dfs(node.right) 

            mid = node == p or node == q

            if mid + left + right >= 2: 
                ans = node 
            
            return mid or left or right 
        
        dfs(root)
        return ans

# Approach 2: Keep Track of Parent Nodes
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [root] 

        parent = {root:None} 

        while p not in parent or q not in parent: 
            node = stack.pop() 

            if node.left: 
                parent[node.left] = node 
                stack.append(node.left) 
            if node.right: 
                parent[node.right] = node 
                stack.append(node.right) 
            
        ancestors = set() 

        while p: 
            ancestors.add(p)
            p = parent[p]
        
        while q not in ancestors: 
            q = parent[q] 
        
        return q

# Approach 3: Iterative without Parent Pointers
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None




class Solution:

    BP = 2
    LD = 1
    BD = 0
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [(root, self.BP)] 

        one_node_found = False 

        LCA_index = -1 

        while stack: 
            parent_node, parent_state = stack[-1]

            if parent_state != self.BD:
                if parent_state == self.BP:
                    if parent_node == p or parent_node == q:
                        if one_node_found: return stack[LCA_index][0]
                        else: 
                            one_node_found = True 
                            LCA_index = len(stack) - 1
                
                    child_node = parent_node.left
                else: 
                    child_node = parent_node.right 
                
                stack.pop()
                stack.append((parent_node, parent_state - 1))

                if child_node: 
                    stack.append((child_node, self.BP))
                
            else: 
                if one_node_found and LCA_index == len(stack) - 1:
                    LCA_index -= 1
                stack.pop()
        
        return None


