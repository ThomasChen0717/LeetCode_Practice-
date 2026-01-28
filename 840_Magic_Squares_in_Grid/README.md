# 840. Magic Squares in Grid

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Array, Matrix, Simulation  

---

## Problem Description

A `3 x 3` **magic square** is a `3 x 3` grid filled with distinct numbers **from** `1` to `9` such that each row, column, and both diagonals all have the same sum.

Given a `row x col` `grid` of integers, how many `3 x 3` magic square subgrids are there?

Note: while a magic square can only contain numbers from 1 to 9, `grid` may contain numbers up to 15.

---

## Examples
Example 1:
![Example 1](https://assets.leetcode.com/uploads/2020/09/11/magic_main.jpg)
```
Input: grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
Output: 1
Explanation: 
The following subgrid is a 3 x 3 magic square:
```
![Example 1 Magic Square](https://assets.leetcode.com/uploads/2020/09/11/magic_valid.jpg)
```
while this one is not:
```
![Example 1 Invalid Magic Square](https://assets.leetcode.com/uploads/2020/09/11/magic_invalid.jpg)
```
In total, there is only one magic square inside the given grid.
```
Example 2:
```
Input: grid = [[8]]
Output: 0
```

## Constraints

- `row == grid.length`
- `col == grid[i].length`
- `1 <= row, col <= 10`
- `0 <= grid[i][j] <= 15`

---

## Approach 1: Brute Force

### Intuition

Define a function to check if a 3 x 3 subgrid starting at `(row, col)` is a magic square. Then we iterate over all possible 3 x 3 subgrids in the grid. 

### Complexity Analysis
Let `M` be the number of rows in the grid and `N` be the number of columns in the grid.
- **Time Complexity:** `O(M * N)`
- **Space Complexity:** `O(1)`

---

## Approach 2: Optimized Brute Force

### Intuition

Same as Approach 1, but we can optimize the check function by using the properties of magic squares. We found that even numbers always appear at corners and 5 is always at the center.  

Furthermore, we found that on the border, the numbers always follow this sequence: 
```
2 9 4 7 5 3 6 1 8
```
clockwise or counterclockwise.

We use these facts to check if a 3 x 3 subgrid is a magic square. If it is, we increment the count.

### Complexity Analysis
- **Time Complexity:** `O(M * N)`
- **Space Complexity:** `O(1)`

---

## Implementation

See `solution.py` for the full implementation.
