# 54. Spiral Matrix

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Matrix, DFS 

---

## Problem Description

Given an `m x n` `matrix`, return all elements of the `matrix` in spiral order.
---

## Examples
Example 1:
![Example 1](https://assets.leetcode.com/uploads/2020/11/13/spiral1.jpg)
```
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
```
Example 2:
![Example 2](https://assets.leetcode.com/uploads/2020/11/13/spiral.jpg)
```
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
```

## Constraints

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 10`
- `-100 <= matrix[i][j] <= 100`

---

## Approach 1: dfs

### Intuition

We use a preorder dfs to traverse the matrix in a spiral order. 
We keep track of current direction index and the directions are ranked as up, right, down, left. 
We use a visited matrix to keep track of visited cells. 

### Complexity Analysis

- **Time Complexity:** `O(mn)`
- **Space Complexity:** `O(mn)`

---

## Approach 2: Update boundary

### Intuition

We simply traverse the matrix in a spiral order. 
We keep track of the boundary of the matrix. 
We update the boundary after we traverse each layer. 

### Complexity Analysis

- **Time Complexity:** `O(mn)`
- **Space Complexity:** `O(1)`

---

## Approach 3: Keep track of visited cells

### Intuition

We simply traverse the matrix in a spiral order. 
We keep track of visited cells. 

### Complexity Analysis

- **Time Complexity:** `O(mn)`
- **Space Complexity:** `O(1)`

---

## Implementation

See `solution.py` for the full implementation.
