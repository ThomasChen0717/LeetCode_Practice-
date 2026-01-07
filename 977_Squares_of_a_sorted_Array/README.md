# 977. Squares of a Sorted Array

**Difficulty:** <span style="color:#2ecc71"><b>Easy</b></span>  
**Topics:** Array, Two Pointers  

---

## Problem Description

Given an integer array `nums` sorted in **non-decreasing** order, return an array of **the squares of each number** sorted in non-decreasing order.

---

## Examples
Example 1:
```
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
```

Example 2:
```
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
``` 

## Constraints

- `1 <= nums.length <= 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `nums` is sorted in **non-decreasing** order.

---

## Approach 1: Sort

### Intuition
Simply square each element in the array and sort the result.

### Complexity Analysis
Let `n` be the length of the array `nums`.
- **Time Complexity:** `O(n log n)`
- **Space Complexity:** `O(n)` or `O(log n)` depending on the sorting algorithm.

---

## Approach 2: Two Pointers

### Intuition
Since the array is sorted in non-decreasing order, the largest squares will be at the ends of the array. We can use two pointers to compare the squares of the elements at the ends and add the larger one to the result array.

### Complexity Analysis
Let `n` be the length of the array `nums`.
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)` if we include the output array, otherwise `O(1)`.

---

## Implementation

See `solution.py` for the full implementation.
