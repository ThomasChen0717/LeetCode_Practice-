# 442. Find All Duplicates in an Array

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Array, Cyclic Sort

---

## Problem Description

Given an integer array `nums` of length `n` where all the integers of `nums` are in the range `[1, n]` and each integer appears **at most twice**, return *an array of all the integers that appears **twice***.

You must write an algorithm that runs in `O(n)` time and uses only *constant* auxiliary space, excluding the space needed to store the output

---

## Examples
Example 1:
```
Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]
```
Example 2:
```
Input: nums = [1,1,2]
Output: [1]
```
Example 3:
```
Input: nums = [1]
Output: []
```

## Constraints

- `n == nums.length`
- `1 <= n <= 10^5`
- `1 <= nums[i] <= n`
- Each element in `nums` appears **once** or **twice**.

---

## Approach 1: Cyclic Sort

### Intuition

We use cyclic sort to put the elements in their correct positions. If an element is not in its correct position, we swap it with the element at its correct position. If an element is already in its correct position, we move to the next element. 

We iterate through the sorted array again and look for elements that are not in their correct positions. If an element is not in its correct position, we add it to the result list.

### Complexity Analysis
Let `n` be the length of the input array `nums`.
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

---

## Approach 2: In-Place Modification

### Intuition

We iterate through the array `nums`. For each element `num`, we check if `nums[abs(num) - 1]` is negative. If it is negative, we add `abs(num)` to the result list. Otherwise, we negate `nums[abs(num) - 1]`.

### Complexity Analysis
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

---

## Implementation

See `solution.py` for the full implementation.
