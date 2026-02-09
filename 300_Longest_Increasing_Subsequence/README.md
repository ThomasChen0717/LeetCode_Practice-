# 300. Longest Increasing Subsequence

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Dynamic Programming, Binary Search

---

## Problem Description

Given an integer array `nums`, return the length of the longest **strictly increasing subsequence**.

---

## Examples
Example 1:
```
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
```
Example 2:
```
Input: nums = [0,1,0,3,2,3]
Output: 4
```
Example 3:
```
Input: nums = [7,7,7,7,7,7,7]
Output: 1
```

## Constraints

- `1 <= nums.length <= 2500`
- `-10^4 <= nums[i] <= 10^4`

---

## Approach 1: Dynamic Programming

### Intuition

We define `dp[i]` as the length of the longest increasing subsequence ending with `nums[i]`. 

We initialize `dp[i] = 1` for all `i` as the minimum length of the increasing subsequence is `1` (the element itself). 

Then we iterate over `i` from `1` to `n-1` and for each `i`, we iterate over `j` from `0` to `i-1`. If `nums[i] > nums[j]`, then we can extend the increasing subsequence ending with `nums[j]` to `nums[i]`, and the length of the subsequence ending with `nums[i]` is `dp[j] + 1`. We take the maximum of all these possible lengths as `dp[i]`.


### Complexity Analysis
Let `n` be the length of `nums`.
- **Time Complexity:** `O(n^2)`
- **Space Complexity:** `O(n)`

---

## Approach 2: Intelligent Build

### Intuition

We can build the longest increasing subsequence incrementally. We maintain a list `sub` that stores the current longest increasing subsequence. For each `num` in `nums`, if `num` is greater than the last element in `sub`, then we append `num` to `sub`. Otherwise, we find the index `i` in `sub` such that `sub[i] >= num` and replace `sub[i]` with `num`. This ensures that `sub` remains the longest increasing subsequence seen so far.

### Complexity Analysis
- **Time Complexity:** `O(n^2)`
- **Space Complexity:** `O(n)`

---

## Approach 3: Intelligent Build + Binary Search

### Intuition

We can further optimize the approach 2 by using binary search to find the index `i` in `sub` such that `sub[i] >= num`. This reduces the time complexity to `O(n log n)`.

### Complexity Analysis
- **Time Complexity:** `O(n log n)`
- **Space Complexity:** `O(n)`

---

## Implementation

See `solution.py` for the full implementation.
