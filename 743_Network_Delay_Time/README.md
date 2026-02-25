# 743. Network Delay Time

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Graph, Dijkstra's Algorithm, Breadth-First Search 

---

## Problem Description

You are given a network of `n` nodes, labeled from `1` to `n`. You are also given `times`, a list of travel times as directed edges `times[i] = (ui, vi, wi)`, where `ui` is the source node, `vi` is the target node, and `wi` is the time it takes for a signal to travel from source to target.

We will send a signal from a given node `k`. Return *the **minimum** time it takes for all the `n` nodes to receive the signal*. If it is impossible for all the `n` nodes to receive the signal, return `-1`.

---

## Examples
Example 1:
![Example 1](https://assets.leetcode.com/uploads/2019/05/23/931_example_1.png)
```
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
```
Example 2:
```
Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
```
Example 3:
```
Input: times = [[1,2,1]], n = 2, k = 2
Output: -1
```

## Constraints

- `1 <= k <= n <= 100`
- `1 <= times.length <= 6000`
- `times[i].length == 3`
- `1 <= ui, vi <= n`
- `ui != vi`
- `0 <= wi <= 100`
- All the pairs `(ui, vi)` are **unique**. (i.e., no multiple edges.)

---

## Approach 1: Breadth-First Search 

### Intuition

We use breadfirst search to find the minimum time it takes for all the `n` nodes to receive the signal. We start from the node `k` and keep track of the time it takes for each node to receive the signal. We only add neighbors if the time it takes to reach the neighbor is less than the current time it takes to reach the neighbor. If we have visited all the nodes, then we return the maximum time it takes for any node to receive the signal. If not, then we return `-1`.

### Complexity Analysis
Let `V` be the number of vertices and `E` be the number of edges in the graph.
- **Time Complexity:** `O(VE)`
- **Space Complexity:** `O(V + E)`

---

## Approach 2: Dijkstra's Algorithm

### Intuition

We use Dijkstra's algorithm to find the minimum time it takes for all the `n` nodes to receive the signal. We start from the node `k` and keep track of the time it takes for each node to receive the signal. We use a priority queue to keep track of the nodes we need to visit next. If we have visited all the nodes, then we return the maximum time it takes for any node to receive the signal. If not, then we return `-1`.

### Complexity Analysis
- **Time Complexity:** `O(E + V log V)`
- **Space Complexity:** `O(E + V)`

---

## Implementation

See `solution.py` for the full implementation.
