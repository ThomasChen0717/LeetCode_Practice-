# 253. Meeting Rooms II

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Heap, Sorting, Chronological Ordering

---

## Problem Description

Given an array of meeting time intervals `intervals` where `intervals[i] = [starti, endi]`, return the minimum number of conference rooms required.

---


## Examples
Example 1:
```
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
```
Example 2:
```
Input: intervals = [[7,10],[2,4]]
Output: 1
```

## Constraints

- `1 <= intervals.length <= 10^4`
- `0 <= starti < endi <= 10^6`

---

## Approach 1: Sorting + Min Heap

### Intuition

We sort the intervals by start time. We then use a min heap to keep track of the end times of the meetings. We iterate through the sorted intervals. If the start time of the current interval is greater than or equal to the end time of the meeting at the top of the heap, then we can reuse the room. Otherwise, we need a new room. We then update the end time of the meeting at the top of the heap to the end time of the current interval. We continue this process until we have iterated through all intervals. The size of the heap at the end is the minimum number of conference rooms required.


### Complexity Analysis

- **Time Complexity:** `O(n log n)`
- **Space Complexity:** `O(n)`

---

## Approach 2: Chronological Ordering

### Intuition

We sort the intervals by start time and end time, obtaining two lists. We then use two pointers to keep track of the start and end times of the meetings. We iterate through the start times. If the start time of the current interval is greater than or equal to the end time of the meeting at the end pointer, then we can reuse the room. Otherwise, we need a new room. We then increment the end pointer. We continue this process until we have iterated through all start times. The number of rooms required is the number of times we need to create a new room.


### Complexity Analysis

- **Time Complexity:** `O(n log n)`
- **Space Complexity:** `O(n)`

---

## Implementation

See `solution.py` for the full implementation.
