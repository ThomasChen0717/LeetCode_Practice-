# 994. Rotting Oranges

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** 2D Array, Breadth-First Search (BFS)

---

## Problem Description

You are given an `m x n` `grid` where each cell can have one of three values:

- 0 representing an empty cell,
- 1 representing a fresh orange, or
- 2 representing a rotten orange.

Every minute, any fresh orange that is **4-directionally adjacent** to a rotten orange becomes rotten.

Return *the minimum number of minutes that must elapse until no cell has a fresh orange.* If this is impossible, return *`-1`*.

---

## Examples
Example 1:
![Example 1](https://assets.leetcode.com/uploads/2019/02/16/oranges.png)
```
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
```
Example 2:
```
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
```
Example 3:
```
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
```

## Constraints

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 10`
- `grid[i][j]` is `0`, `1`, or `2`.

---

## Approach 1: BFS

### Intuition

Find the rotten oranges at time 0. Then, for each rotten orange, spread the rot to its adjacent fresh oranges. Keep track of the time it takes for all fresh oranges to become rotten(this is the level of BFS). If there are any fresh oranges that remain, return `-1`. Otherwise, return the time it took for all fresh oranges to become rotten.

### Complexity Analysis

- **Time Complexity:** `O(mn)`
- **Space Complexity:** `O(mn)`

---

## Approach 2: Constant Space at cost of time 

### Intuition

We can use the input grid to store the time it takes for each orange to become rotten. We can use the value `2` to represent a rotten orange and the value `0` to represent an empty cell. We can use the values `2` to `m*n + 2` to represent the time it takes for each fresh orange to become rotten.

For each timestamp, we iterate through the whole matrix, spreading the rotten oranges corresponding to the timestamp to its adjacent fresh oranges. If there are any fresh oranges that remain, we return `-1`. Otherwise, we return the time it took for all fresh oranges to become rotten minus 2.

### Complexity Analysis

- **Time Complexity:** `O(m^2n^2)`
- **Space Complexity:** `O(1)`

---

## Implementation

See `solution.py` for the full implementation.
