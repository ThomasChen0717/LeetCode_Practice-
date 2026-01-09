# 525. Contiguous Array

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** HashMap, Prefix Sum

---

## Problem Description

Given a binary array `nums`, return the maximum length of a contiguous subarray with an equal number of `0` and `1`.

---

## Examples
Example 1:
```
Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
```
Example 2:
```
Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
```
Example 3:
```
Input: nums = [0,1,1,1,1,1,0,0,0]
Output: 6
Explanation: [1,1,1,0,0,0] is the longest contiguous subarray with equal number of 0 and 1.
```
 

## Constraints

- `1 <= nums.length <= 10^5`
- `nums[i]` is either `0` or `1`.

---

## Approach: Prefix Sum with HashMap

### Intuition

Two cases: 
- If the subarray starts from the beginning of the array, the prefix sum is 0. 
- If the subarray does not start from the beginning of the array, then the prefix sum at the beginning of the subarray is the same as the prefix sum at the end of the subarray. 
    - We can use a hashmap to store the prefix sum and its index. If we encounter the same prefix sum, then the subarray between the two indices has an equal number of 0 and 1.
    - We only update the hashmap with the first occurrence of each prefix sum. 
    - The maximum length of the subarray is the difference between the current index and the index stored in the hashmap.

### Complexity Analysis
Let `n` be the length of the array.
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

---

## Implementation

See `solution.py` for the full implementation.
