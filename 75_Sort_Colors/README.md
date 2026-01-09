# 75. Sort Colors

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Array, Three Pointers, Sorting  

---

## Problem Description

Given an array `nums` with `n` objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers `0`, `1`, and `2` to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

---

## Examples
Example 1:
```
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
```
Example 2:
```
Input: nums = [2,0,1]
Output: [0,1,2]
```

## Constraints

- `n == nums.length`
- `1 <= n <= 300`
- `nums[i]` is either `0`, `1`, or `2`.

---

## Approach 1: Counting Sort

### Intuition

Simple brute force approach. 
Count the number of 0s, 1s, and 2s in the array.
Then, overwrite the array with the correct number of 0s, 1s, and 2s.

### Complexity Analysis
Let `n` be the length of the array.
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

---

## Approach 2: One Pass Three Pointers

### Intuition

We can use three pointers to solve this problem.
We can use `curr` to iterate through the array.
We can use `p0` to keep track of the position of the next 0.
We can use `p2` to keep track of the position of the next 2.
If `nums[curr] == 0`, then we swap `nums[curr]` with `nums[p0]` and increment `p0` and `curr`. 
    - Position is finalized
If `nums[curr] == 2`, then we swap `nums[curr]` with `nums[p2]` and decrement `p2`.
If `nums[curr] == 1`, then we increment `curr`.

### Complexity Analysis
Let `n` be the length of the array.
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

---

## Implementation

See `solution.py` for the full implementation.
