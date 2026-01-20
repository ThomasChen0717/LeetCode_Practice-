# 189. Rotate Array

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Array, Math, Two Pointers

---

## Problem Description

Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.

 

---

## Examples
Example 1:
```
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
```
Example 2:
```
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
```

## Constraints

- `1 <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `0 <= k <= 10^5`

---

## Approach 1: Brute Force

### Intuition

Simply do `k` rotations.

### Complexity Analysis
Let `n` be the length of `nums`, and `k` be the number of rotations.
- **Time Complexity:** `O(n * k)`
- **Space Complexity:** `O(1)`

---

## Approach 2: Using Extra Array

### Intuition

We can use an extra array to store the rotated array. 

Each element `nums[i]` will be moved to `nums[(i + k) % n]`, where `n` is the length of `nums`.

### Complexity Analysis
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

---

## Approach 3: Using Cyclic Replacements

### Intuition

We can rotate the array in-place using cyclic replacements. 
We keep the original element and replace it with the element at the next position. 
We follow to the next position and repeat the process.
When we reach the original position, we start the process again with the next element. 

### Complexity Analysis
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

---

## Approach 4: Using Reverse

### Intuition

We can reverse the entire array, then reverse the first `k` elements, and finally reverse the rest of the array.

### Complexity Analysis
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

---

## Implementation

See `solution.py` for the full implementation.
