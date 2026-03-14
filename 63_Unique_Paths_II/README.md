# 63. Unique Paths II

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Array, Dynamic Programming, Matrix

---

## Problem Description

You are given an `m x n` integer array `grid`. There is a robot initially located at the **top-left corner** (i.e., `grid[0][0]`). The robot tries to move to the **bottom-right corner** (i.e., `grid[m - 1][n - 1]`). The robot can only move either down or right at any point in time.

An obstacle and space are marked as `1` or `0` respectively in `grid`. A path that the robot takes cannot include **any** square that is an obstacle.

Return *the number of possible unique paths that the robot can take to reach the bottom-right corner*.

The testcases are generated so that the answer will be less than or equal to `2 * 10^9`.

---

## Examples
**Example 1:** 
![Example 1](https://assets.leetcode.com/uploads/2020/11/04/robot1.jpg)
```
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid. From the top-left corner, there are a total of 2 ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
```

**Example 2:**
![Example 2](https://assets.leetcode.com/uploads/2020/11/04/robot2.jpg)
```
Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
```

## Constraints

- `m == obstacleGrid.length`
- `n == obstacleGrid[i].length`
- `1 <= m, n <= 100`
- `obstacleGrid[i][j]` is `0` or `1`.

---

## Approach 1: Plain DFS (Brute Force)

### Intuition

This approach uses a simple recursive depth-first search (DFS) to explore all possible paths. The function `dfs(i, j)` calculates the number of unique paths from cell `(i, j)` to the destination.

From any cell, the robot can move right `(i, j+1)` or down `(i+1, j)`. So, the total paths from `(i, j)` are the sum of paths from these two cells. The recursion stops if it goes out of bounds, hits an obstacle, or reaches the destination.

This method is easy to conceptualize but is highly inefficient as it re-computes the number of paths for the same cells multiple times.

### Complexity Analysis

- **Time Complexity:** `O(2^(m*n))`. In the worst case, we explore a large number of paths, leading to exponential complexity.
- **Space Complexity:** `O(m+n)` for the recursion stack depth.

---

## Approach 2: Memoization (Top-Down DP)

### Intuition

To optimize the plain DFS, we can use memoization to store the results of subproblems. We create a `memo` table to keep track of the number of paths from each cell `(i, j)`.

Before computing `dfs(i, j)`, we first check if the result is already in our `memo` table. If it is, we return the stored value. Otherwise, we compute it, store it in the table, and then return it. This ensures that the number of paths for each cell is calculated only once.

### Complexity Analysis

- **Time Complexity:** `O(m*n)`. Each cell is visited once.
- **Space Complexity:** `O(m*n)` for the memoization table and recursion stack.

---

## Approach 3: Bottom-Up DP

### Intuition

This approach uses a 2D DP table where `dp[i][j]` represents the number of unique paths to reach cell `(i, j)`. The number of ways to reach `dp[i][j]` is the sum of the ways to reach the cell above it, `dp[i-1][j]`, and the cell to its left, `dp[i][j-1]`.

The base case is `dp[0][0]`, which is `1` if the start cell is not an obstacle. If any cell `(i, j)` contains an obstacle, `dp[i][j]` is set to `0`.

We fill the table iteratively from top-left to bottom-right. The final answer is the value in `dp[n-1][m-1]`.

### Complexity Analysis

- **Time Complexity:** `O(m*n)`. We iterate through the entire grid once.
- **Space Complexity:** `O(m*n)` for the DP table.

---

## Approach 4: DP with Constant Space (In-Place)

### Intuition

This is a space-optimized version of the bottom-up DP. Instead of creating a separate DP table, we can reuse the `obstacleGrid` itself to store the number of paths. The logic remains the same as the standard bottom-up DP, but we update the grid in-place.

If a cell `obstacleGrid[i][j]` is an obstacle (`1`), we set its path count to `0`. Otherwise, we calculate the paths based on the updated values from the cells above and to the left.

This approach saves space but modifies the input grid.

### Complexity Analysis

- **Time Complexity:** `O(m*n)`.
- **Space Complexity:** `O(1)`, as we are not using any extra space proportional to the input size.

---

## Implementation

See `solution.py` for the full implementation of all four approaches.
