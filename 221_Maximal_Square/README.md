# 221. Maximal Square

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Array, Dynamic Programming, Matrix

---

## Problem Description

Given an `m x n` binary matrix filled with `0`'s and `1`'s, find the largest square containing only `1`'s and *return its area*.

---

## Examples
**Example 1:** 
![Example 1](https://assets.leetcode.com/uploads/2020/11/26/max1grid.jpg)
```
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4
```

**Example 2:**
![Example 2](https://assets.leetcode.com/uploads/2020/11/26/max2grid.jpg)
```
Input: matrix = [["0","1"],["1","0"]]
Output: 1
```

**Example 3:**
```
Input: matrix = [["0"]]
Output: 0
```

## Constraints

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 300`
- `matrix[i][j]` is '`0`' or '`1`'.

---

## Approach 1: 2D Dynamic Programming

### Intuition

This problem can be solved efficiently using dynamic programming. The core idea is to define a DP state `dp[i][j]` that represents the side length of the largest square of all `1`'s whose **bottom-right corner** is at `matrix[i-1][j-1]`.

If `matrix[i-1][j-1]` is `'0'`, no square can end there, so `dp[i][j] = 0`. 

If `matrix[i-1][j-1]` is `'1'`, a square can be formed. The size of this square is limited by its neighbors. Specifically, to form a square of side `s` ending at `(i-1, j-1)`, we must have squares of at least side `s-1` ending at the adjacent cells: `(i-2, j-1)` (up), `(i-1, j-2)` (left), and `(i-2, j-2)` (diagonal). 

This gives us the recurrence relation:
`dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1`

We build a `(n+1)x(m+1)` DP table, iterate through the matrix, and apply this logic. The maximum value found in the `dp` table will be the side length of the largest square. The final answer is this length squared.

### Complexity Analysis

-   **Time Complexity:** `O(m * n)`, as we iterate through each cell of the matrix once.
-   **Space Complexity:** `O(m * n)` to store the DP table.

---

## Approach 2: 1D Dynamic Programming (Space Optimized)

### Intuition

We can optimize the space complexity of the previous approach. Notice that to compute the values for the current row `i`, we only need the values from the previous row `i-1`. This suggests we can reduce the 2D DP table to a 1D array.

We use a 1D `dp` array of size `m+1`. As we iterate through row `i`, `dp[j]` will store the value that would have been `dp[i-1][j]` in the 2D approach. The value `dp[j-1]` holds the value for `dp[i][j-1]`. 

The tricky part is accessing the diagonal element, `dp[i-1][j-1]`. Before we overwrite `dp[j]` with the new value for the current row, it still holds the value from the previous row. We need to store this `dp[i-1][j-1]` value (which corresponds to the old `dp[j-1]` before the inner loop's update) in a temporary variable, let's call it `prev`.

The recurrence relation becomes:
If `matrix[i-1][j-1] == '1'`, then `dp[j] = min(dp[j], dp[j-1], prev) + 1`.

We iterate through the matrix, updating the 1D `dp` array and the `prev` variable in place, and keep track of the maximum side length found.

### Complexity Analysis

-   **Time Complexity:** `O(m * n)`. The time complexity remains the same.
-   **Space Complexity:** `O(m)`, where `m` is the number of columns. We use a 1D array to store the results of the previous row.

---

## Implementation

See [`solution.py`](file:///c:\Users\thoma\Documents\Leetcode\221_Maximal_Square\solution.py) for the full implementation of both approaches.
