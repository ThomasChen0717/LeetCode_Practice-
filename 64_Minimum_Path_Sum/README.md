# 64. Minimum Path Sum

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Dynamic Programming

---

## Problem Description

Given a `m x n` `grid` filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

**Note**: You can only move either down or right at any point in time.

---

## Examples
Example 1:
![Example 1](https://assets.leetcode.com/uploads/2020/11/05/minpath.jpg)
```
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
```
Example 2:
```
Input: grid = [[1,2,3],[4,5,6]]
Output: 12
```
## Constraints

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 200`
- `0 <= grid[i][j] <= 200`

---

## Approach 1: 2D Bottom-Up Dynamic Programming

### Intuition

Each block computes the min at that block by adding the value at the block and the minimum of its left and top neighbors. Handle edge cases where such neighbors do not exist. At the end, the minimum path sum to the bottom right block will simply be the value stored in the dp at the index `m-1`, `n-1`.  

### Complexity Analysis

- **Time Complexity:** `O(mn)`
- **Space Complexity:** `O(mn)`

---

## Approach 2: 1D Bottom-Up Dynamic Programming

### Intuition

Same as Approach 1, but instead of using a 2D dp array, we can use a 1D dp array to store the minimum path sum to each block in the current row. The top block has not been overwritten yet and the left block has been computed. 

### Complexity Analysis

- **Time Complexity:** `O(mn)`
- **Space Complexity:** `O(n)`

---

## Approach 3: Constant Space Dynamic Programming

### Intuition

Same as Approach 2, but instead of using a 1D dp array, we can use the grid itself to store the minimum path sum to each block in the current row. 

### Complexity Analysis

- **Time Complexity:** `O(mn)`
- **Space Complexity:** `O(1)`

---

## Implementation

See `solution.py` for the full implementation.
