# 1288. Remove Covered Intervals

**Difficulty:** <span style="color:#f1c40f"><b>Medium</b></span>  
**Topics:** Array, Sorting

---

## Problem Description

Given an array `intervals` where `intervals[i] = [li, ri]` represent the interval `[li, ri)`, remove all intervals that are covered by another interval in the list.

The interval `[a, b)` is covered by the interval `[c, d)` if and only if `c <= a` and `b <= d`.

Return _the number of remaining intervals_.

---

## Examples

**Example 1:**
```
Input: intervals = [[1,4],[3,6],[2,8]]
Output: 2
Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
```

**Example 2:**
```
Input: intervals = [[1,4],[2,3]]
Output: 1
```

## Constraints

- `1 <= intervals.length <= 1000`
- `intervals[i].length == 2`
- `0 <= li < ri <= 10^5`
- All the given intervals are **unique**.

---

## Approach: Greedy with Sorting

### Intuition

The problem asks us to count the number of intervals that are not covered by any other interval. A brute-force approach of comparing every pair of intervals would be `O(n^2)`, which might be too slow. A more efficient approach involves sorting.

The key idea is to sort the intervals in a specific way that allows us to easily identify covered intervals in a single pass. If we sort the intervals primarily by their start points, we can iterate through them and keep track of the maximum end point seen so far.

Consider two intervals, `A = [a, b)` and `C = [c, d)`. `C` covers `A` if `c <= a` and `b <= d`.

If we sort by the start point `a` in ascending order, any interval `C` that could cover the current interval `A` must have appeared before `A` in the sorted list (or have the same start point). This simplifies our check.

Now, what if two intervals have the same start point, like `[3, 8)` and `[3, 6)`? The one with the larger end point, `[3, 8)`, can cover the other. If we process the larger one first, we can easily determine that `[3, 6)` is covered. This leads to our sorting strategy: 

1.  Sort by start point in ascending order.
2.  If start points are the same, sort by end point in **descending** order.

With this sorting, we can iterate through the sorted intervals and maintain a variable `max_end` representing the maximum end point of the intervals processed so far that were not covered. For each new interval, if its end point is less than or equal to `max_end`, it must be covered. Why? Because we sorted by start point, the current interval's start is greater than or equal to the start of the interval that set the `max_end`. Since its end is also less than or equal to `max_end`, it is fully contained.

### Algorithm

1.  Sort the `intervals` array. The primary sort key is the start point (ascending), and the secondary sort key is the end point (descending).
2.  Initialize `max_end = 0` (or negative infinity) to keep track of the maximum end point of the non-covered intervals seen so far.
3.  Initialize a `count` of covered intervals to `0`.
4.  Iterate through the sorted intervals:
    -   For each `interval`, if its end point `interval[1]` is less than or equal to `max_end`, it means this interval is covered by a previous one. Increment `count`.
    -   Otherwise, this interval is not covered. We update `max_end` to be the end point of this new, larger-reaching interval.
5.  The number of remaining intervals is `len(intervals) - count`.

### Complexity Analysis

-   **Time Complexity:** `O(n log n)`, dominated by the initial sort of the intervals.
-   **Space Complexity:** `O(log n)` or `O(n)`, depending on the implementation of the sorting algorithm used. In Python, Timsort uses `O(n)` space in the worst case.

---

## Implementation

See `solution.py` for the full implementation.