# 3534. Path Existence Queries in a Graph II

**Difficulty:** <span style="color:#c0392b"><b>Hard</b></span>  
**Topics:** Graph, Two Pointers, Sorting, Binary Lifting

---

## Problem Description

You are given an integer `n` representing the number of nodes in a graph, labeled from `0` to `n - 1`. You are also given an integer array `nums` of length `n` and an integer `maxDiff`.

An **undirected** edge exists between nodes `i` and `j` if the **absolute** difference between `nums[i]` and `nums[j]` is **at most** `maxDiff` (i.e., `|nums[i] - nums[j]| <= maxDiff`).

You are also given a 2D integer array `queries`. For each `queries[i] = [ui, vi]`, find the **minimum distance** between nodes `ui` and `vi`. If no path exists between the two nodes, return `-1` for that query.

Return an array `answer`, where `answer[i]` is the result of the `ith` query.

**Note:** The edges between the nodes are unweighted.

---

## Examples

**Example 1:**
```
Input: n = 5, nums = [1,8,3,4,2], maxDiff = 3, queries = [[0,3],[2,4]]
Output: [1,1]
```

**Example 2:**
```
Input: n = 5, nums = [5,3,1,9,10], maxDiff = 2, queries = [[0,1],[0,2],[2,3],[4,3]]
Output: [1,2,-1,1]
```

## Constraints

- `1 <= n == nums.length <= 10^5`
- `0 <= nums[i] <= 10^5`
- `0 <= maxDiff <= 10^5`
- `1 <= queries.length <= 10^5`
- `queries[i] == [ui, vi]`
- `0 <= ui, vi < n`

---

## Approach: Two Pointers + Binary Lifting

### Intuition

The problem asks for the shortest path between nodes in an implicitly defined graph. A direct BFS for each query would be too slow (`O(Q * (N+E))`) because the number of edges `E` can be large and there are many queries.

The core idea is to re-frame the problem to answer queries more efficiently. Instead of working with the given node indices, we can work with the nodes sorted by their `nums` value. In this sorted arrangement, the edge condition `|nums[i] - nums[j]| <= maxDiff` is easier to handle.

Let's consider the nodes in their sorted order. For any node `y`, a path can be formed by jumping to other nodes. A single step in a path can be thought of as a "jump". To find the shortest path from node `u` to `v`, we need to find the minimum number of jumps. The challenge is that a jump can go from a node `i` to any node `j` that satisfies the `maxDiff` condition.

To simplify this, we can define a specific type of jump. For each node `i` in the sorted list, let's find the single best "parent" node it can jump from. A good candidate for a parent of `i` is the leftmost node `j` (`j < i`) such that `nums[i] - nums[j] <= maxDiff`. This creates a directed parent-pointer structure. Finding the path from `u` to `v` now means finding how many jumps it takes to get from one to an ancestor of the other.

This structure, where each node has a single parent, is a tree (or a forest). The problem of finding the number of steps between two nodes on this tree can be solved efficiently using **Binary Lifting** (also known as sparse table or jump pointers).

### Algorithm

1.  **Sort and Map:**
    -   Since the `nums` array is unsorted, we first sort it to handle the `maxDiff` condition efficiently. We don't sort `nums` itself, but rather create a sorted list of indices `idx` based on their corresponding values in `nums`.
    -   Create a `pos` array to map each original node index to its position in the sorted `idx` list.

2.  **Build Parent Pointers (`f[i][0]`):**
    -   We create a binary lifting table `f[i][j]`, where `f[i][j]` stores the `2^j`-th ancestor of the node at sorted position `i`.
    -   To start, we compute the direct parent `f[i][0]` for each node `i`.
    -   We use a **two-pointer** approach (`left`) on the sorted nodes. For each node `i` (from left to right), we advance `left` such that `left` is the smallest index where `nums[idx[i]] - nums[idx[left]] > maxDiff` is violated. This `left` becomes the parent of `i`, so we set `f[i][0] = left`.

3.  **Build Binary Lifting Table:**
    -   Fill the rest of the table using the recurrence: `f[i][j] = f[ f[i][j-1] ][j-1]`. This means the `2^j`-th ancestor is the `2^(j-1)`-th ancestor of the `2^(j-1)`-th ancestor.

4.  **Process Queries:**
    -   For each query `(u, v)`:
        a.  Find their positions in the sorted list: `x = pos[u]` and `y = pos[v]`. Assume `x < y` without loss of generality.
        b.  The goal is to find the minimum number of jumps to get from `y` to an ancestor that is at or before `x`.
        c.  Use the binary lifting table to jump from `y` upwards as far as possible without passing `x`. Iterate `j` from `log(n)` down to `0`. If the `2^j`-th ancestor `f[y][j]` is still greater than `x`, it's a safe jump. We take the jump (`y = f[y][j]`) and add `2^j` to our `step` count.
        d.  After the loop, we are at a node `y` whose direct parent `f[y][0]` is guaranteed to be `<= x`.
        e.  If `f[y][0] <= x`, we can reach the target region in one final step. The total steps are `step + 1`.
        f.  If `f[y][0] > x`, it's impossible to bridge the gap, so no path exists. The result is `-1`.

### Complexity Analysis

-   **Time Complexity:** `O((n+q) * log(n))`. 
    -   `O(n log n)` to sort the indices.
    -   `O(n)` to build the parent pointers (`f[i][0]`) using the two-pointer method.
    -   `O(n log n)` to build the full binary lifting table.
    -   `O(q log n)` to answer all queries.
-   **Space Complexity:** `O(n log n)` for storing the binary lifting table `f`.

---

## Implementation

See `solution.py` for the full implementation.