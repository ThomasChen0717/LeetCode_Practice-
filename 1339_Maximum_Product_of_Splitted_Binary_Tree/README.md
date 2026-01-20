# 1339. Maximum Product of Splitted Binary Tree

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Bit Manipulation, Tree, Depth-First Search

---

## Problem Description

Given the `root` of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.

Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo `10^9 + 7`.

Note that you need to maximize the answer before taking the mod and not after taking it.

---

## Examples
Example 1:
![Example 1](https://assets.leetcode.com/uploads/2020/01/21/sample_1_1699.png)
```
Input: root = [1,2,3,4,5,6]
Output: 110
Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)
```
Example 2:
![Example 2](https://assets.leetcode.com/uploads/2020/01/21/sample_2_1699.png)
```
Input: root = [1,null,2,3,4,null,null,5,6]
Output: 90
Explanation: Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)
```

## Constraints

- The number of nodes in the tree is in the range `[2, 5 * 10^4]`.
- `1 <= Node.val <= 10^4`

---

## Approach 1: One Pass DFS

### Intuition

We can calculate the whole tree sum in the first pass of DFS. Then, for each node, we can calculate the sum of the subtree rooted at that node. We store all subtree sums in a list. 
The other subtree sum is the total sum minus the sum of the current subtree.
We can then iterate over all subtree sums and calculate the product of the sum of the two subtrees. We return the maximum product modulo `10^9 + 7`.

### Complexity Analysis

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

---

## Approach 2: Two Pass DFS

### Intuition

We can calculate the whole tree sum in the first pass of DFS. 
Then, in the second pass, for each node, we can calculate the sum of the subtree rooted at that node. We compare the product of the sum of the current subtree and the other subtree sum with the maximum product found so far.
We return the maximum product modulo `10^9 + 7`.

### Complexity Analysis

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

---

## Approach 3: Advanced Strategies for Dealing with 32-Bit Integers

### Intuition

We can use the fact that the product of two numbers is maximized when they are close to each other.
We use modular multiplication to avoid overflow.

### Complexity Analysis

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

---

## Implementation

See `solution.py` for the full implementation.
