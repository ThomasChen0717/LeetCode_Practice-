# 360. Sort Transformed Array

**Difficulty:** <span style="color:#2ecc71"><b>Medium</b></span>  
**Topics:** Sorting, Two Pointers 

---

## Problem Description

Given a **sorted** integer array `nums` and three integers `a`, `b` and `c`, apply a quadratic function of the form `f(x) = ax^2 + bx + c` to each element `nums[i]` in the array, and return *the array in a sorted order*.

---

## Examples
Example 1:
```
Input: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
Output: [3,9,15,33]
```
Example 2:
```
Input: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
Output: [-23,-5,1,7]
```

## Constraints

- `1 <= nums.length <= 200`
- `100 <= nums[i], a, b, c <= 100`
- `nums` is sorted in **ascending** order.

---

## Approach 1: Brute Force Sorting

### Intuition

Basically compute the quadratic function for each element in the array, and sort the array.

### Complexity Analysis

- **Time Complexity:** `O(n log n)`
- **Space Complexity:** `O(n)` or `O(log n)` depending on the sorting algorithm used.

---

## Approach 2: Two Pointers

### Intuition
We find that if `a` is negative, then further away from the origin, the quadratic function will decrease. Therefore, we can use two pointers to compare the quadratic values of the elements at the left and right ends of the array, and add the smaller one to the result array. If `a` is positive, then further away from the origin, the quadratic function will increase. Therefore, we can use two pointers to compare the quadratic values of the elements at the left and right ends of the array, and add the larger one to the result array, and reverse at the end.  

### Complexity Analysis

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

## Implementation

See `solution.py` for the full implementation.
