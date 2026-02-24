# 200. Number of Islands

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Depth-First Search, Breadth-First Search, Union Find, Matrix

---

## Problem Description

Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return *the number of islands*.

An **island** is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

---

## Examples
Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

## Constraints

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 300`
- `grid[i][j]` is `'0'` or `'1'`.

---

## Approach 1: Depth-First Search (DFS)
 
### Intuition

Do a DFS search on each land cell not visited. If the cell is `'1'`, increment the island count and mark the cell as visited by changing it to `'0'`.

### Complexity Analysis

- **Time Complexity:** `O(m * n)`, where `m` is the number of rows and `n` is the number of columns in the grid.
- **Space Complexity:** `O(m * n)` in the worst case, where the grid is filled with `'1'`s.

---

## Approach 2: Breadth-First Search (BFS)

### Intuition

Do a BFS search on each land cell not visited. If the cell is `'1'`, increment the island count and mark the cell as visited by changing it to `'0'`.

### Complexity Analysis

- **Time Complexity:** `O(m * n)`, where `m` is the number of rows and `n` is the number of columns in the grid.
- **Space Complexity:** `O(min(m, n))` in the worst case, where the grid is filled with `'1'`s.

---

## Approach 3: Union Find

### Intuition

Use Union Find data structure to merge adjacent land cells. The number of islands is the number of connected components in the Union Find data structure.

### Complexity Analysis

- **Time Complexity:** `O(m * n)`, where `m` is the number of rows and `n` is the number of columns in the grid.
- **Space Complexity:** `O(m * n)` in the worst case, where the grid is filled with `'1'`s.

---

## Implementation

See `solution.py` for the full implementation.
