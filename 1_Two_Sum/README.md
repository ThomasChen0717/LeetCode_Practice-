# 1. Two Sum

**Difficulty:** <span style="color:#2ecc71"><b>Easy</b></span>  
**Topics:** HashTable

---

## Problem Description

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have **exactly one solution**, and you may not use the same element twice.

You can return the answer in any order.

---

## Examples
Example 1:
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```
Example 2:
```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```
Example 3:
```
Input: nums = [3,3], target = 6
Output: [0,1]
```

## Constraints

- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- **Only one valid answer exists.**

---

## Approach: Simple Brute Force 

### Intuition

Loop through each pair of numbers in the array and check if their sum equals the target. 

### Key Observations

- <Observation 1>
- <Observation 2>
- <Observation 3>

### Complexity Analysis

- **Time Complexity:** `O(n^2)`
- **Space Complexity:** `O(1)`

---

## Approach: One Pass Hash Table

### Intuition

Loop through the array once. For each number, check if the complement (target - number) exists in the hash table. If it does, return the indices of the two numbers. Otherwise, add the number to the hash table.

### Complexity Analysis

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

---

## Implementation

See `solution.py` for the full implementation.
