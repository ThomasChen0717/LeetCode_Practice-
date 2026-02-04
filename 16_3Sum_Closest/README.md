# 16. 3Sum Closest

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Arrays, Sorting, Two Pointers

---

## Problem Description

Given an integer array `nums` of length `n` and an integer `target`, find three integers in `nums` such that the sum is closest to `target`.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

---

## Examples
Example 1:
```
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
```
Example 2:
```
Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
```

## Constraints

- `3 <= nums.length <= 500`
- `-1000 <= nums[i] <= 1000`
- `-10^4 <= target <= 10^4`

---

## Approach: Sorting and Two Pointers

### Intuition

To find the sum of three integers closest to the target, we can sort the array first. This allows us to use the two-pointer technique to efficiently find the closest sum. We keep iterating through the array, for each element `nums[i]`, we use two pointers `left` and `right` to represent the two numbers we want to find such and update min diff it by comparing to `target - nums[i]`. 

### Complexity Analysis
Let `n` be the length of the array.
- **Time Complexity:** `O(n^2)` 
- **Space Complexity:** `O(n)` or `O(log n)` depending on the sorting algorithm.

---

## Implementation

See `solution.py` for the full implementation.
