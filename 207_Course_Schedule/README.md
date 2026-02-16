# 207. Course Schedule

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Graph, Topological Sort, DFS

---

## Problem Description

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [a_i, b_i]` indicates that you must take course `b_i` first if you want to take course `a_i`.

For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.
Return `true` if you can finish all courses. Otherwise, return `false`.

---

## Examples
Example 1:
```
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
```
Example 2:
```
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
```

## Constraints

- `1 <= numCourses <= 2000`
- `0 <= prerequisites.length <= 5000`
- `prerequisites[i].length == 2`
- `0 <= a_i, b_i < numCourses`
- All the pairs `prerequisites[i]` are unique.

---

## Approach 1: Topological Sort(Kahn's Algorithm)

### Intuition

We start with nodes with indegree 0 and remove them from the graph. We continue this process until all nodes are removed. If there are still nodes in the graph, then there is a cycle in the graph. 

### Complexity Analysis
Let `n` be the number of courses and `m` be the number of prerequisites.
- **Time Complexity:** `O(n + m)`
- **Space Complexity:** `O(n + m)`

---

## Approach 2: Depth-First Search(DFS)

### Intuition

We can use DFS to detect cycles in the graph. We start with a node and mark it as visited. We then recursively visit all its neighbors. If we visit a node that is already visited in the current path, then there is a cycle in the graph.

### Complexity Analysis
- **Time Complexity:** `O(n + m)`
- **Space Complexity:** `O(n + m)`

---

## Implementation

See `solution.py` for the full implementation.
