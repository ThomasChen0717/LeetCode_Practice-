# 51. N-Queens

**Difficulty:** <span style="color:#e74c3c"><b>Hard</b></span>  
**Topics:** Backtracking

---

## Problem Description

The ****n-queens** puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other.

Given an integer `n`, return *all distinct solutions to the **n-queens puzzle***. You may return the answer in **any order**.

Each solution contains a distinct board configuration of the n-queens' placement, where `'Q'` and `'.'` both indicate a queen and an empty space, respectively.

---

## Examples
**Example 1:** 
![Example 1](https://assets.leetcode.com/uploads/2020/11/13/queens.jpg)

```
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
```

**Example 2:**
```
Input: n = 1
Output: [["Q"]]
```

## Constraints

- `1 <= n <= 9`

---

## Approach: Backtracking

### Intuition

The problem asks for all possible valid placements of N queens on an N×N board, which suggests that we need to explore multiple potential solutions. This is a classic combinatorial problem that can be solved using a backtracking algorithm.

The core idea is to place queens one by one, row by row. For each row, we try to place a queen in every possible column. Before placing a queen, we must check if that position is safe—meaning it is not under attack by any previously placed queens. A position `(row, col)` is under attack if another queen exists in the same column, or on the same main diagonal or anti-diagonal.

To efficiently check for attacks, we can use sets to keep track of occupied columns, diagonals, and anti-diagonals:
-   **Columns:** A column is identified simply by its index `col`.
-   **Diagonals:** For any cell `(row, col)`, all cells on the same main diagonal have a constant value for `row - col`.
-   **Anti-diagonals:** Similarly, all cells on the same anti-diagonal have a constant value for `row + col`.

The backtracking function proceeds as follows:
1.  Start at `row = 0`.
2.  Iterate through each `col` from `0` to `n-1`.
3.  For the current `(row, col)`, check if the corresponding column, diagonal, and anti-diagonal are already occupied.
4.  If the position is safe, "place" the queen by adding the column and diagonal identifiers to our sets and marking the position on the board.
5.  Recursively call the function for the next row (`row + 1`).
6.  After the recursive call returns, "remove" the queen (backtrack) by removing the identifiers from the sets and resetting the board position. This allows us to explore other possibilities for the current row.

When we successfully place a queen in the last row (`row == n`), it means we have found a valid solution. At this point, we format the current board state and add it to our list of results.

### Complexity Analysis

-   **Time Complexity:** `O(N!)`. The problem is about finding all permutations of queen placements. In the first row, we have `N` choices. In the second, we have at most `N-1` choices, and so on. While pruning from the backtracking reduces the search space, the complexity remains factorial in nature.
-   **Space Complexity:** `O(N^2)`. We need `O(N^2)` space to store the board. The sets used for tracking occupied columns and diagonals take `O(N)` space, and the recursion depth is `O(N)`. Therefore, the board size dominates the space complexity.

---

## Implementation

See `solution.py` for the full implementation.
