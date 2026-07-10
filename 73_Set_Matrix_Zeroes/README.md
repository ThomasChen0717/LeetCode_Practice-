# 73. Set Matrix Zeroes

**Difficulty:** <span style="color:#f1c40f"><b>Medium</b></span>  
**Topics:** Array, Hash Table, Matrix

---

## Problem Description

Given an `m x n` integer matrix `matrix`, if an element is `0`, set its entire row and column to `0`'s.

You must do it [in place](https://en.wikipedia.org/wiki/In-place_algorithm).

---

## Examples

**Example 1:**
```
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
```

**Example 2:**
```
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
```

## Constraints

- `m == matrix.length`
- `n == matrix[0].length`
- `1 <= m, n <= 200`
- `-2^31 <= matrix[i][j] <= 2^31 - 1`

---

## Approach 1: Use First Row and Column as Markers (Two Flags)

### Intuition

The problem requires a constant space solution, which means we cannot use extra arrays to keep track of rows and columns to be zeroed. The key idea is to use the matrix itself as storage.

We can use the first row and the first column as markers. If a cell `matrix[i][j]` is `0`, we can mark its corresponding row and column by setting `matrix[i][0] = 0` and `matrix[0][j] = 0`.

However, this creates an ambiguity for the cell `matrix[0][0]`. Does `matrix[0][0] = 0` mean the first row should be zeroed, or the first column? To resolve this, we use two separate boolean flags, `flag_row0` and `flag_col0`, to track the status of the first row and first column independently.

### Algorithm

1.  **Check First Row/Column:** Create two boolean flags, `flag_row0` and `flag_col0`. Iterate through the first row and first column to determine if they originally contain any zeros. Set the flags accordingly.

2.  **Mark Using First Row/Column:** Iterate through the rest of the matrix (from `matrix[1][1]`). If you find a zero at `matrix[i][j]`, set `matrix[i][0] = 0` and `matrix[0][j] = 0`.

3.  **Set Zeros based on Markers:** Iterate through the rest of the matrix again (from `matrix[1][1]`). If the marker in the first row `matrix[0][j]` or the first column `matrix[i][0]` is `0`, then set `matrix[i][j] = 0`.

4.  **Set First Row/Column:** Finally, use the `flag_row0` and `flag_col0` from step 1 to set the first row and first column to zeros if needed.

### Complexity Analysis

-   **Time Complexity:** `O(m * n)`, as we traverse the matrix a constant number of times.
-   **Space Complexity:** `O(1)`, as we only use two boolean flags for storage.

---

## Approach 2: Optimized Space (One Flag)

### Intuition

We can optimize the space from two flags to one. We can use the `matrix[0][0]` cell to serve as the marker for the first row, but we still need a separate flag for the first column. This is because the `matrix[0][0]` cell is shared by both the first row and the first column, and we can't let it do double duty without an extra flag.

Let's use `flag_col0` to track the state of the first column. The first cell of each other row, `matrix[i][0]`, can track the state of row `i`. The first cell of each other column, `matrix[0][j]`, can track the state of column `j`.

### Algorithm

1.  **Initialize First Column Flag:** Create a boolean flag, `flag_col0`, and check if any cell in the first column is `0`. If so, set `flag_col0 = True`.

2.  **Mark First Row/Column:** Iterate through the matrix starting from the second column (`j=1`). If `matrix[i][j]` is `0`, set its corresponding markers `matrix[i][0] = 0` and `matrix[0][j] = 0`. Note that the first column is only used as a marker for its respective row and is not modified by other columns in this step.

3.  **Set Zeros (from bottom-right):** To avoid overwriting our markers in the first row and column before we've used them, we should iterate backwards from the bottom-right corner of the matrix (excluding the first row and column). For each cell `matrix[i][j]`, if `matrix[i][0] == 0` or `matrix[0][j] == 0`, set `matrix[i][j] = 0`.

4.  **Handle First Row and Column:** Check if `matrix[0][0]` is `0`. If it is, zero out the entire first row. Then, if `flag_col0` is true, zero out the entire first column.

The solution in the Python code is a slight variation where the backward loop is combined with setting the first column, but the principle is the same: process the main matrix before altering the first column marker.

### Complexity Analysis

-   **Time Complexity:** `O(m * n)`.
-   **Space Complexity:** `O(1)`.

---

## Implementation

See `solution.py` for the full implementation of both approaches.