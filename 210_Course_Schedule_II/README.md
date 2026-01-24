# 210. Course Schedule II

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Graph, Topological Sort, DFS, BFS

---

## Problem Description

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [a_i, b_i]` indicates that you **must** take course `b_i` first if you want to take course `a_i`.

- For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.

Return the ordering of courses you should take to finish all courses. If there are many valid answers, return **any** of them. If it is impossible to finish all courses, return **an empty array**.

---

## Examples
Example 1:
```
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
```
Example 2:
```
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
```
Example 3:
```
Input: numCourses = 1, prerequisites = []
Output: [0]
```

## Constraints

- `1 <= numCourses <= 2000`
- `0 <= prerequisites.length <= numCourses * (numCourses - 1)`
- `prerequisites[i].length == 2`
- `0 <= a_i, b_i < numCourses`
- `a_i != b_i`
- All the pairs `[a_i, b_i]` are **distinct**.

---

## Approach 1: Topological Sort with DFS

### Intuition

For this problem, we can use a topological sort algorithm to find the order of courses. 
We first create an adjacency list to represent the graph of courses and prerequisites. 

For each of the courses, we try to do a depth-first search (DFS) to find a topological order if it has not been visited. 

If we encounter a cycle during the DFS, it means that it is impossible to finish all courses.  

We use three colors to represent the visiting status of each course during the DFS:
- `WHITE`: The course has not been visited.
- `GRAY`: The course is being visited.
- `BLACK`: The course has been visited.

Cycle happens when we encounter a course that is currently being visited, during the DFS. 
In this case, it is impossible to finish all courses.  

After reaching a course without any unvisited neighbors, we mark it as `BLACK` and add it to the result list. 

The result list contains the courses in the topological order. 
We reverse the list to get the correct order.  

### Complexity Analysis
Let 
- `V` be the number of courses.
- `E` be the number of prerequisites.
- **Time Complexity:** `O(V + E)` 
  - adj_list: `O(E)`
  - dfs: `O(V + E)`
- **Space Complexity:** `O(V + E)`
  - adj_list: `O(E)`
  - color: `O(V)`
  - res: `O(V)`

---
## Approach 2: Using Node Indegree

### Intuition

We can also use a node indegree approach to find the topological order. 
We first create an adjacency list to represent the graph of courses and prerequisites. 
We also create a list to store the indegree of each course. 

We then add all courses with indegree `0` to a queue. 
We process each course in the queue, and for each course, we reduce the indegree of its neighbors by `1`. 
If a neighbor's indegree becomes `0`, we add it to the queue. 

We continue this process until the queue is empty. 
If the number of processed courses is equal to the total number of courses, it means that it is possible to finish all courses. 
Otherwise, it is impossible to finish all courses.  

### Complexity Analysis
Let 
- `V` be the number of courses.
- `E` be the number of prerequisites.
- **Time Complexity:** `O(V + E)` 
  - adj_list: `O(E)`
  - indegree: `O(E)`
  - bfs: `O(V + E)`
- **Space Complexity:** `O(V + E)`
  - adj_list: `O(E)`
  - indegree: `O(V)`
  - q: `O(V)`



## Implementation

See `solution.py` for the full implementation.
