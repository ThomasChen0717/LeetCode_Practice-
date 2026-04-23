# 1848. Minimum Distance to the Target Element

**Difficulty:** <span style="color:#2ecc71"><b>Easy</b></span>  
**Topics:** Array

---

## Problem Description

Given an integer array `nums` (0-indexed) and two integers `target` and `start`, find an index `i` such that `nums[i] == target` and `abs(i - start)` is minimized. Note that `abs(x)` is the absolute value of `x`.

Return `abs(i - start)`.

It is guaranteed that `target` exists in `nums`.

---

## Examples

**Example 1:**
```
Input: nums = [1,2,3,4,5], target = 5, start = 3
Output: 1
```
**Explanation:** `nums[4] = 5` is the only value equal to target, so the answer is `abs(4 - 3) = 1`.

**Example 2:**
```
Input: nums = [1], target = 1, start = 0
Output: 0
```
**Explanation:** `nums[0] = 1` is the only value equal to target, so the answer is `abs(0 - 0) = 0`.

**Example 3:**
```
Input: nums = [1,1,1,1,1,1,1,1,1,1], target = 1, start = 0
Output: 0
```
**Explanation:** Every value of `nums` is 1, but `nums[0]` minimizes `abs(i - start)`, which is `abs(0 - 0) = 0`.

## Constraints

- `1 <= nums.length <= 1000`
- `1 <= nums[i] <= 10^4`
- `0 <= start < nums.length`
- `target` is in `nums`.

---

## Approach: Linear Scan

### Intuition

The problem asks for the minimum distance from a given `start` index to an index containing a `target` value. Since we need to find the *minimum* distance, we must consider all occurrences of the `target` element in the array.

The most straightforward and efficient way to solve this is to iterate through the entire array. We can maintain a variable, `min_distance`, initialized to a very large value (infinity). As we scan through the array, every time we encounter the `target` element at an index `i`, we calculate the distance `abs(i - start)` and update `min_distance` if this new distance is smaller than the current `min_distance`.

Since the problem guarantees that the `target` element exists in the array, we are sure to find at least one valid distance. After checking all elements, the final value of `min_distance` will be our answer.

### Complexity Analysis

- **Time Complexity:** `O(N)`, where `N` is the length of the `nums` array. We perform a single pass through the array.
- **Space Complexity:** `O(1)`. We only use a single variable to keep track of the minimum distance, which requires constant extra space.

---

## Implementation

See `solution.py` for the full implementation.
