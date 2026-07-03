# 3620. Network Recovery Pathways

**Difficulty:** <span style="color:#c0392b"><b>Hard</b></span>  
**Topics:** Binary Search, Graph, Topological Sort, Shortest Path, Dijkstra, Dynamic Programming

---

## Problem Description

You are given a directed acyclic graph (DAG) of `n` nodes numbered from `0` to `n - 1`. You are also given a list of `edges`, where `edges[i] = [ui, vi, costi]` indicates a one-way communication from node `ui` to `vi` with a recovery `costi`.

A boolean array `online` of length `n` is also provided, where `online[i]` is true if the `i-th` node is online and false otherwise.

The **path score** of a path is the **minimum** recovery cost of any edge in that path.

Find the **maximum path score** of a valid path from node `0` to node `n - 1`. A path is considered valid if:
1. All nodes on the path are online.
2. The total recovery cost (sum of all edge costs) on the path does not exceed a given integer `k`.

If no valid path exists, return `-1`.

---

## General Approach: Binary Search on the Answer

All three solutions leverage the same core idea: **binary search on the path score**. The problem asks for the *maximum possible minimum edge weight* (path score). This structure suggests that we can binary search for the answer.

Let's say we want to check if a path score of `mid` is possible. This means we need to determine if there exists a path from node `0` to `n - 1` that satisfies two conditions:
1.  Every edge on the path must have a weight of at least `mid`.
2.  The sum of the weights of the edges on this path must be less than or equal to `k`.

This transforms the problem into a decision problem: for a given `mid`, does such a path exist? This is a shortest path problem on a subgraph. We only consider nodes that are online and edges with `weight >= mid`. Our goal is to find if the shortest path in this subgraph has a total cost `<= k`.

If `check(mid)` is true, it means a score of `mid` is achievable, so we try for a higher score (`l = mid + 1`). If it's false, we must lower our expectations (`r = mid - 1`).

The overall algorithm is:
1.  Initialize search range `[l, r]` for the path score.
2.  Binary search within this range.
3.  For each `mid`, run a `check(mid)` function.
4.  Based on the result of `check(mid)`, adjust the search range.

The three provided solutions differ in how they implement the `check(mid)` function.

---

## Approach 1: Binary Search + Dijkstra's Algorithm

### Intuition

For the `check(mid)` function, we need to find the shortest path from `0` to `n-1` in the graph where we only use edges with `weight >= mid`. Dijkstra's algorithm is a standard and robust way to find the single-source shortest path in a weighted graph with non-negative edge weights.

### Algorithm

1.  **`check(mid)` function:**
2.  Initialize a `distances` array with infinity, with `distances[0] = 0`.
3.  Use a min-priority queue and push the starting node `(0, 0)` (distance, node).
4.  While the priority queue is not empty, extract the node with the smallest distance.
5.  If the extracted distance is greater than `k` or we have already found a shorter path to this node, skip.
6.  If the node is the destination (`n-1`), we have found a valid path, so `check(mid)` returns `true`.
7.  For each neighbor of the current node, if the edge weight is `>= mid`, relax the edge by updating the neighbor's distance if a shorter path is found.
8.  If the loop finishes and we haven't reached the destination, it means no path exists under the current constraints, so return `false`.

### Complexity Analysis

-   **Time Complexity:** `O(E * log(max_weight) * log(N))`, where `E` is the number of edges and `N` is the number of nodes. The binary search contributes `log(max_weight)`. Inside the search, Dijkstra's algorithm runs in `O(E * log(N))`. 
-   **Space Complexity:** `O(N + E)` for storing the adjacency list and the distances.

---

## Approach 2: Binary Search + Memoization DFS

### Intuition

Since the graph is a Directed Acyclic Graph (DAG), we can also find the shortest path using dynamic programming or recursion with memoization. This can be more efficient than Dijkstra's if the graph structure is favorable.

The `check(mid)` function can be implemented as a recursive DFS that finds the minimum cost to travel from any `node` to the destination `n-1`.

### Algorithm

1.  **`check(mid)` function:**
2.  Create a `memo` array to store the results of the DFS to avoid re-computing shortest paths from the same node.
3.  Define a `dfs(node)` function that returns the minimum cost from `node` to `n-1`.
4.  **Base Case:** If `node == n-1`, the cost is `0`.
5.  **Memoization:** If `memo[node]` is already computed, return it.
6.  **Recursive Step:** Initialize a result `res` to infinity. For each neighbor `v` of `node` with edge weight `w >= mid`, recursively call `dfs(v)` and update `res = min(res, dfs(v) + w)`.
7.  Store and return `res` in `memo[node]`.
8.  The main `check` function returns `true` if `dfs(0) <= k`.

### Complexity Analysis

-   **Time Complexity:** `O(E * log(max_weight))`. The binary search contributes `log(max_weight)`. The DFS with memoization on a DAG runs in `O(N + E)`, as each node and edge is visited once.
-   **Space Complexity:** `O(N + E)` for the adjacency list, memoization table, and recursion stack.

---

## Approach 3: Binary Search + Topological DP

### Intuition

This is the most optimized approach for a DAG. Instead of a top-down DFS, we can use a bottom-up dynamic programming approach based on a topological sort of the graph. We process nodes in an order such that for any edge `u -> v`, `u` is always processed before `v`. This allows us to compute shortest paths iteratively.

### Algorithm

1.  **Preprocessing:** Before the binary search, perform a topological sort to establish a processing order and prune nodes that are not reachable from the source (or cannot reach the destination), which can optimize the `check` function.
2.  **`check(mid)` function:**
3.  Initialize a `dp` array (distances) with infinity, with `dp[0] = 0`.
4.  Create a queue for the topological sort and add the starting node `0`.
5.  Maintain an in-degree count for each node in the subgraph (considering only edges with `weight >= mid`).
6.  Process nodes from the queue in topological order.
7.  For each node `u`, iterate through its neighbors `v`. If the edge `u -> v` has `weight >= mid`, relax the edge: `dp[v] = min(dp[v], dp[u] + w)`.
8.  Decrement the in-degree of `v`. If it becomes 0, add `v` to the queue.
9.  After the loop, `dp[n-1]` will hold the shortest path cost. `check(mid)` returns `true` if `dp[n-1] <= k`.

### Complexity Analysis

-   **Time Complexity:** `O(E * log(max_weight))`. Similar to the DFS approach, the check function runs in linear time `O(N + E)` for a DAG.
-   **Space Complexity:** `O(N + E)` for the adjacency list, `dp` array, and in-degree counts.

---

## Implementation

See `solution.py` for the full implementation of all three approaches.