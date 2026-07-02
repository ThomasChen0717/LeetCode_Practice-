# 3286. Find a Safe Walk Through a Grid

**Difficulty:** <span style="color:#f1c40f"><b>Medium</b></span>  
**Topics:** Breadth-First Search, Graph, Array, Matrix, Shortest Path, Heap (Priority Queue)

---

## Problem Description

You are given an `m x n` binary matrix `grid` and an integer `health`.

You start on the upper-left corner `(0, 0)` and would like to get to the lower-right corner `(m - 1, n - 1)`.

You can move up, down, left, or right from one cell to another adjacent cell as long as your health _remains_ **positive**.

Cells `(i, j)` with `grid[i][j] = 1` are considered **unsafe** and reduce your health by 1. Cells with `grid[i][j] = 0` are safe and do not affect your health.

Return `true` if you can reach the final cell with a health value of 1 or more, and `false` otherwise.

---

## Examples

**Example 1:**
```
Input: grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]], health = 1
Output: true
```

**Example 2:**
```
Input: grid = [[0,1,1,0,0,0],[1,0,1,0,0,0],[0,1,1,1,0,1],[0,0,1,0,1,0]], health = 3
Output: false
```

**Example 3:**
```
Input: grid = [[1,1,1],[1,0,1],[1,1,1]], health = 5
Output: true
```

## Constraints

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 50`
- `2 <= m * n`
- `1 <= health <= m + n`
- `grid[i][j]` is either 0 or 1.

---

## Approach 1: Dijkstra's Algorithm

### Intuition

This problem can be framed as finding the shortest path in a weighted graph. The grid cells are the nodes, and the cost of traversing an edge to a cell is given by `grid[i][j]`. We want to find the path from `(0, 0)` to `(m-1, n-1)` with the minimum total cost (health reduction).

Dijkstra's algorithm is a perfect fit for this. We can use a priority queue to always explore the path with the minimum accumulated cost so far.

### Algorithm

1.  Initialize a `distance` matrix with -1 to store the minimum cost to reach each cell.
2.  Use a min-priority queue to store tuples of `(cost, x, y)`.
3.  Push the starting cell `(grid[0][0], 0, 0)` onto the priority queue.
4.  While the priority queue is not empty, pop the cell with the minimum cost.
5.  If this cell has already been visited (i.e., `distance[x][y]` is not -1), continue.
6.  Mark the cell as visited by setting `distance[x][y]` to the current cost.
7.  Explore all four adjacent neighbors. For each neighbor, if it's within the grid boundaries and not visited, push `(current_cost + neighbor_cost, nx, ny)` to the priority queue.
8.  After the algorithm terminates, the minimum cost to reach the destination `(m-1, n-1)` will be stored in `dis[m-1][n-1]`.
9.  Return `true` if this minimum cost is less than the initial `health`, otherwise return `false`.

### Complexity Analysis

-   **Time Complexity:** `O(m * n * log(m * n))`, where `m` and `n` are the dimensions of the grid. Each cell is pushed and popped from the priority queue at most once.
-   **Space Complexity:** `O(m * n)` for the `distance` matrix and the priority queue.

---

## Approach 2: 0-1 BFS (Dequq)

### Intuition

Since the edge weights are only 0 or 1, we can use a specialized version of BFS known as 0-1 BFS. This is generally more efficient than Dijkstra's for graphs with only two edge weights.

A 0-1 BFS uses a deque (double-ended queue). When we traverse an edge with weight 0, we add the new node to the front of the deque. When we traverse an edge with weight 1, we add the new node to the back. This ensures that we always process the paths with lower costs first, similar to Dijkstra's but without the overhead of a priority queue.

### Algorithm

1.  Initialize a `distance` matrix with infinity to store the minimum cost to reach each cell.
2.  Use a deque and add the starting cell `(0, 0)`.
3.  Set `distance[0][0]` to `grid[0][0]`.
4.  While the deque is not empty, pop a cell from the left.
5.  If we reach the destination, we can return `true` if the cost is less than `health`. (The provided solution has a slight variation on this, checking for path feasibility during exploration).
6.  Explore all four adjacent neighbors.
7.  For each neighbor, calculate the `new_cost`.
8.  If the `new_cost` is less than the current `distance` to that neighbor and also less than `health`:
    *   Update `distance[nx][ny]` to `new_cost`.
    *   If the cost to enter the neighbor cell (`grid[nx][ny]`) is 1, add the neighbor to the back of the deque.
    *   If the cost is 0, add the neighbor to the front of the deque.
9.  If the loop finishes without reaching the destination under the health constraint, return `false`.

### Complexity Analysis

-   **Time Complexity:** `O(m * n)`. Each cell is added to and removed from the deque at most once.
-   **Space Complexity:** `O(m * n)` for the `distance` matrix and the deque.

---

## Implementation

See `solution.py` for the full implementation of both approaches.