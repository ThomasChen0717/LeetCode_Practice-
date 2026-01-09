# 1161. Maximum Level Sum of a Binary Tree

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Binary Tree, Breadth-First Search(BFS), Depth-First Search(DFS)

---

## Problem Description

Given the `root` of a binary tree, the level of its root is `1`, the level of its children is `2`, and so on.

Return the **smallest** level `x` such that the sum of all the values of nodes at level `x` is **maximal**.

 

---

## Examples
Example 1:
```
Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
```
Example 2:
```
Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2
```

## Constraints

- The number of nodes in the tree is in the range `[1, 10^4]`.
- `-10^5 <= Node.val <= 10^5`

---

## Approach 1: Breadth-First Search (BFS)

### Intuition

Since we are computing the sum of nodes at each level, we can use BFS to traverse the tree level by level. 
At each level, we compute the sum of nodes and update the maximum sum and level if necessary.

### Complexity Analysis

- **Time Complexity:** `O(n)` where `n` is the number of nodes in the tree.
- **Space Complexity:** `O(n)` where `n` is the number of nodes in the tree.

## Approach 2: Depth-First Search (DFS)

### Intuition

We can also use DFS to traverse the tree. 
We use an extra array `sum_of_nodes_at_level` to store the sum of nodes at each level. 
At each node, we update the sum of nodes at the corresponding level in the array.

### Complexity Analysis

- **Time Complexity:** `O(n)` where `n` is the number of nodes in the tree.
- **Space Complexity:** `O(n)` where `n` is the number of nodes in the tree.

---

## Implementation

See `solution.py` for the full implementation.
