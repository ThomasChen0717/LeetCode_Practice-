# 34. Find First and Last Position of Element in Sorted Array

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Array, Binary Search

---

## Problem Description

Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value.

If `target` is not found in the array, return `[-1, -1]`.

You must write an algorithm with `O(log n)` runtime complexity.

---

## Examples
Example 1:
```
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
```
Example 2:
```
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
```
Example 3:
```
Input: nums = [], target = 0
Output: [-1,-1]
```

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- `nums` is a non-decreasing array.
- `-10^9 <= target <= 10^9`

---

## Approach: Binary Search to find left and right boundary, two binary searches

### Intuition

For the binary search function, take in an extra boolean `isFirst` to indicate whether we are searching for the first occurrence or the last occurrence. 
- If `isFirst` is `True`, we are searching for the first occurrence.
- If `isFirst` is `False`, we are searching for the last occurrence.
Then we run two binary searches:
- The first binary search to find the left boundary.
- The second binary search to find the right boundary. 

### Complexity Analysis

- **Time Complexity:** `O(log n)`
- **Space Complexity:** `O(1)`

---

## Implementation

See `solution.py` for the full implementation.
