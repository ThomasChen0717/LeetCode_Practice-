# 236. Lowest Common Ancestor of a Binary Tree

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Binary Tree, DFS

---

## Problem Description

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants (where we allow **a node to be a descendant of itself**).”

---

## Examples
Example 1:
![Example 1](https://assets.leetcode.com/uploads/2018/12/14/binarytree.png)
```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
```
Example 2:
![Example 2](https://assets.leetcode.com/uploads/2018/12/14/binarytree.png)
```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
```
Example 3:

```
Input: root = [1,2], p = 1, q = 2
Output: 1
```

## Constraints

- The number of nodes in the tree is in the range `[2, 10^5]`.
- `-10^9 <= Node.val <= 10^9`
- All `Node.val` are **unique**.
- `p` and `q` are different nodes and both values `p` and `q` will exist in the tree.

---
 
## Approach 1: DFS Recursive

### Intuition

We can use a depth-first search (DFS) approach to find the LCA. 
We keep `left`, `right`, and `mid` flags to track whether `p` and `q` are found in the left subtree, right subtree, and the current node, respectively. 
If `mid + left + right >= 2`, it means that `p` and `q` are found in different subtrees, and the current node is the LCA.
Otherwise, we return `True` if either left or right child or `mid` is `True`, and `False` otherwise.

### Complexity Analysis

- **Time Complexity:** `O(N)`
- **Space Complexity:** `O(N)`

---

## Approach 2: Keep Track of Parent Nodes

### Intuition

We use iterative approach to traverse the tree. 
We keep a stack to store the nodes to visit. 
We also keep a dictionary to store the parent of each node. 
We start from the root node, and for each node, we add its left and right children to the stack if they exist. 
We also update the parent dictionary. 
We continue this process until we find both `p` and `q`. 

Once we find both `p` and `q`, we use the parent dictionary to find the LCA. 
We keep a set to store the ancestors of `p`. 
We start from `p` and keep adding its parent to the set until we reach the root node. 
We then keep moving up `q` until we find a node that is in the set of `p`'s ancestors. 
This node is the LCA. 

### Complexity Analysis

- **Time Complexity:** `O(N)`
- **Space Complexity:** `O(N)`

---
## Approach 3: Iterative without Parent Pointers

### Intuition

We use iterative approach to traverse the tree in a post-order manner. 
We keep a stack to store the nodes to visit. 
In the stack, we keep three states for each node:
- `BP`: The node is Both Pending.
- `LD`: The node is Left Done.
- `BD`: The node is Both Done.

We start from the root node, and for each node, we add it to the stack with state `BP`. 

We pop when the top of the stack is `BD`. 
This means that we have visited both children of the node. 

When we find the first target node, we set the `LCA_index` to the current index in the stack. 

When we backtrack, we need to also update the `LCA_index`.

When we find the second target node, we can return the value at the `LCA_index` in the stack. 

### Complexity Analysis

- **Time Complexity:** `O(N)`
- **Space Complexity:** `O(N)`

---


## Implementation

See `solution.py` for the full implementation.
