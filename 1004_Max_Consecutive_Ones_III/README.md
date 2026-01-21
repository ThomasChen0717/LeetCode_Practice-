# 1004. Max Consecutive Ones III

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Array, Sliding Window  

---
## Problem Description
Given a binary array nums and an integer `k`, return the maximum number of consecutive 1's in the array if you can flip at most `k` 0's.

---

## Examples
Example 1: 
```
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
```
Example 2: 
```
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
```

## Constraints
- `1 <= nums.length <= 10^5`
- `nums[i]` is either `0` or `1`.
- `0 <= k <= nums.length`

---

## Approach 1: Sliding Window

### Intuition
We use a sliding window approach to find the maximum number of consecutive 1's. The window expands by including new elements and contracts when the number of 0's exceeds `k`.

### Correctness Argument 
This always give the correct result because the window always expands to include more 1's and contracts to ensure the number of 0's does not exceed `k`. It keeps the maximum number of consecutive 1's found so far.

### Complexity Analysis
n is the length of the array `nums`.
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`  

---

## Implementation

See `solution.py` for the full implementation.
