# 120. Triangle

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Array, Dynamic Programming

---

## Problem Description

Given a `triangle` array, return *the minimum path sum from top to bottom*.

For each step, you may move to an adjacent number on the row below. More formally, if you are on index `i` on the current row, you may move to either index `i` or index `i + 1` on the next row.

---

## Examples
**Example 1:** 
```
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11.
```

**Example 2:**
```
Input: triangle = [[-10]]
Output: -10
```

## Constraints

- `1 <= triangle.length <= 200`
- `triangle[0].length == 1`
- `triangle[i].length == triangle[i - 1].length + 1`
- `-10^4 <= triangle[i][j] <= 10^4`

---

## Approach 1: Dynamic Programming (Bottom-Up, In-Place)

### Intuition

This approach modifies the input `triangle` to store the minimum path sum to reach each cell. We can think of each cell's value as being updated to the minimum cost to arrive at that cell from the top.

The algorithm iterates from the second row to the bottom. For each cell `(i, j)`, the minimum path sum to reach it is its own value plus the minimum of the path sums of the cells above it that can lead to it. These are `(i-1, j-1)` and `(i-1, j)`.

After iterating through the entire triangle, the last row will contain the total minimum path sums to reach each of its cells. The minimum value in this last row is the overall minimum path sum for the triangle.

### Complexity Analysis

-   **Time Complexity:** `O(N^2)`, where `N` is the number of rows in the triangle. We visit each cell once.
-   **Space Complexity:** `O(1)`, as we modify the triangle in-place and do not use any extra space proportional to the input size.

---

## Approach 2: Dynamic Programming (Bottom-Up, O(N) Space)

### Intuition

This is a more space-optimized bottom-up approach. Instead of modifying the original triangle or using an `N x N` DP table, we can notice that to compute the minimum path sums for a row, we only need the results from the row immediately below it.

This algorithm starts from the second-to-last row and works its way up to the top. It uses an array (e.g., `prev_row`) that initially holds the values of the last row of the triangle. It then computes a `curr_row` for the row above it, where `curr_row[j] = triangle[i][j] + min(prev_row[j], prev_row[j+1])`.

By the time we reach the top of the triangle, the first element of our `prev_row` array will hold the overall minimum path sum.

### Complexity Analysis

-   **Time Complexity:** `O(N^2)`.
-   **Space Complexity:** `O(N)` to store the results for one row of the triangle.

---

## Approach 3: Dynamic Programming (Top-Down, Memoization)

### Intuition

This approach uses recursion with memoization to solve the problem from the top down. We define a recursive function, `min_path(row, col)`, that calculates the minimum path sum starting from cell `(row, col)` down to the bottom.

The recursive relation is:
`min_path(row, col) = triangle[row][col] + min(min_path(row + 1, col), min_path(row + 1, col + 1))`

The base case for the recursion is any cell in the last row, where the minimum path sum is just the value of the cell itself.

To avoid recomputing the same subproblems, we use a memoization table (a 2D array) to store the results of `min_path(row, col)` once they are computed. The final answer is the result of `min_path(0, 0)`.

### Complexity Analysis

-   **Time Complexity:** `O(N^2)`. Each state `(row, col)` is computed only once thanks to memoization.
-   **Space Complexity:** `O(N^2)` for the memoization table and the recursion stack.

---

## Implementation

See `solution.py` for the full implementation.
