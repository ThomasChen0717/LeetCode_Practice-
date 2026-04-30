# 3742. Maximum Path Score in a Grid

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Array, Dynamic Programming, Matrix

---

## Problem Description

You are given an `m x n` grid where each cell contains one of the values 0, 1, or 2. You are also given an integer `k`.

You start from the top-left corner `(0, 0)` and want to reach the bottom-right corner `(m - 1, n - 1)` by moving only right or down.

Each cell contributes a specific score and incurs an associated cost, according to their cell values:
- **0:** adds 0 to your score and costs 0.
- **1:** adds 1 to your score and costs 1.
- **2:** adds 2 to your score and costs 1.

Return the maximum score achievable without exceeding a total cost of `k`, or -1 if no valid path exists.

**Note:** If you reach the last cell but the total cost exceeds `k`, the path is invalid.

---

## Examples

**Example 1:**
```
Input: grid = [[0, 1],[2, 0]], k = 1
Output: 2
```
**Explanation:**
The optimal path is (0, 0) -> (1, 0) -> (1, 1). The total score is 0 + 2 + 0 = 2, and the total cost is 0 + 1 + 0 = 1, which does not exceed `k`.

**Example 2:**
```
Input: grid = [[0, 1],[1, 2]], k = 1
Output: -1
```
**Explanation:**
There is no path that reaches cell (1, 1) without exceeding cost `k`.

## Constraints

- `1 <= m, n <= 200`
- `0 <= k <= 1000`
- `grid[0][0] == 0`
- `0 <= grid[i][j] <= 2`

---

## Approach 1: Brute-Force DFS

### Intuition

The problem asks for the maximum score of a path from the top-left to the bottom-right of a grid, with movement restricted to right and down, and a total cost constraint. A natural way to explore all possible paths is using Depth-First Search (DFS).

We can define a recursive function `dfs(i, j, k, current_score)` that explores paths starting from cell `(i, j)` with a remaining cost `k` and a `current_score`. In each step, we calculate the cost of the current cell. If the remaining cost `k` is sufficient, we subtract the cost, add the cell's value to our score, and recursively call the function for the cells to the right `(i, j+1)` and down `(i+1, j)`.

When the DFS reaches the bottom-right corner, we have found a valid path. We then update a global maximum score with the score of this path. If at any point the cost exceeds `k`, we prune that path.

While correct, this approach is highly inefficient. It will re-explore the same cell `(i, j)` with the same remaining cost `k` multiple times, leading to an exponential number of computations. This will result in a "Time Limit Exceeded" (TLE) error for larger grids.

### Complexity Analysis

- **Time Complexity:** `O(2^(m+n))`. In the worst case, the number of paths can be exponential.
- **Space Complexity:** `O(m+n)` for the recursion stack depth.

---

## Approach 2: Memoization DFS (Top-Down DP)

### Intuition

To optimize the brute-force DFS, we can use memoization to avoid re-computing results for the same states. This is a top-down dynamic programming approach.

The state of our DFS can be uniquely identified by the current position `(i, j)` and the remaining cost `k`. Therefore, we can define our DP state as `dp(i, j, k)`, representing the maximum score we can get from this point onwards to the destination.

We use a 3D array, `memo[i][j][k]`, to store the result of `dfs(i, j, k)`. Before computing the result for a state, we check if it's already in our memoization table. If it is, we return the stored value. Otherwise, we compute the result, store it in the table, and then return it.

The recursive function `dfs(i, j, k)` will work as follows:
1.  Handle base cases: If we are out of bounds or `k` is negative, the path is invalid, so we return a very small number (or -1) to signify this.
2.  Check memoization table: If `memo[i][j][k]` has been computed, return it.
3.  Handle destination: If we are at the bottom-right corner, the score from this point is just the value of the current cell.
4.  Recursive step: Recursively call `dfs` for the right and down cells with the updated remaining cost `k`. The score for the current state will be `grid[i][j]` plus the maximum score returned from the recursive calls.
5.  Store and return: Store the computed result in `memo[i][j][k]` and return it.

This approach avoids redundant calculations and efficiently finds the maximum path score.

### Complexity Analysis

- **Time Complexity:** `O(m * n * k)`. We compute the result for each state `(i, j, k)` only once.
- **Space Complexity:** `O(m * n * k)` for the memoization table and recursion stack.

---

## Implementation

See `solution.py` for the full implementation of both approaches.
