# Approach 1: One Pass DFS 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        all_sums = []


        def tree_sum(node): 
            if node is None: return 0 
            left_sum = tree_sum(node.left)
            right_sum = tree_sum(node.right) 

            total_sum = left_sum + right_sum + node.val 
            all_sums.append(total_sum)
            return total_sum 

        
        total = tree_sum(root) 
        best = 0 
        for s in all_sums: 
            best = max(best, s * (total - s))
        
        return best % (10 ** 9 + 7)

# Approach 2: Two Pass DFS 
def maxProduct(self, root: TreeNode) -> int:

    def tree_sum(subroot):
        if subroot is None: return 0
        left_sum = tree_sum(subroot.left)
        right_sum = tree_sum(subroot.right)
        return left_sum + right_sum + subroot.val

    def maximum_product(subroot, total):
        best = 0
        def recursive_helper(subroot):
            nonlocal best
            if subroot is None: return 0
            left_sum = recursive_helper(subroot.left)
            right_sum = recursive_helper(subroot.right)
            total_sum = left_sum + right_sum + subroot.val
            product = total_sum * (tree_total_sum - total_sum)
            best = max(best, product)
            return total_sum
        recursive_helper(subroot)
        return best

    tree_total_sum = tree_sum(root)
    return maximum_product(root, tree_total_sum) % (10 ** 9 + 7)

## Approach 3: Advanced Strategies for Dealing with 32-Bit Integers
class Solution:
    MOD = 10**9 + 7

    def __init__(self):
        self.allSums = []

    def maxProduct(self, root: Optional['TreeNode']) -> int:
        totalSum = self.treeSum(root)

        nearestToHalf = 0
        smallestDistanceBetween = float('inf')

        for s in self.allSums:
            # Minimize |totalSum - 2 * s| to avoid floats
            distanceBetween = abs(totalSum - 2 * s)
            if distanceBetween < smallestDistanceBetween:
                smallestDistanceBetween = distanceBetween
                nearestToHalf = s

        return self.modularMultiplication(
            nearestToHalf,
            totalSum - nearestToHalf,
            self.MOD
        )

    def modularMultiplication(self, a: int, b: int, m: int) -> int:
        product = 0
        currentSum = a

        while b > 0:
            if b & 1:
                product = (product + currentSum) % m
            currentSum = (currentSum << 1) % m
            b >>= 1

        return product

    def treeSum(self, node: Optional['TreeNode']) -> int:
        if not node:
            return 0

        leftSum = self.treeSum(node.left)
        rightSum = self.treeSum(node.right)

        total = leftSum + rightSum + node.val
        self.allSums.append(total)

        return total
