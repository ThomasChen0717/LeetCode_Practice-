# 56_Merge_Intervals 

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Graph, Sortiong, Array

---

## Problem Description

Given an array of `intervals` where `intervals[i] = [starti, endi]`, merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

---

## Examples
Example 1:
```
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
```
Example 2:
```
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
```
Example 3:
```
Input: intervals = [[4,7],[1,4]]
Output: [[1,7]]
Explanation: Intervals [1,4] and [4,7] are considered overlapping.
```

## Constraints

- `1 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= starti <= endi <= 10^4`

---

## Approach 1: Brute Force Graph

### Intuition

Use a graph to represent the intervals. 
Each interval is a node, and an edge exists between two nodes if they overlap. 
We can then use a graph traversal algorithm (e.g., DFS) to find all connected components and merge them.

### Complexity Analysis

- **Time Complexity:** `O(n^2)`
- **Space Complexity:** `O(n^2)`

---

## Approach 2: Sorting

### Intuition

Sort the intervals by their start times. 
Then, iterate through the sorted intervals and merge overlapping ones.

### Complexity Analysis

- **Time Complexity:** `O(n log n)`
- **Space Complexity:** `O(n)` or `O(log n)` depending on the language's sorting algorithm.

---

## Implementation

See `solution.py` for the full implementation.
