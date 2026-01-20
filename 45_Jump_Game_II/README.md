# 45. Jump Game II

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Array, Dynamic Programming, Greedy

---

## Problem Description

You are given a `0-indexed` array of integers `nums` of length `n`. You are initially positioned at index 0.

Each element `nums[i]` represents the maximum length of a forward jump from index `i`. In other words, if you are at index `i`, you can jump to any index `(i + j)` where:

- `0 <= j <= nums[i]` and
- `i + j < n`

Return the minimum number of jumps to reach index `n - 1`. The test cases are generated such that you can reach index `n - 1`.

---

## Examples
Example 1:
```
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last 
index.
```
Example 2:
```
Input: nums = [2,3,0,1,4]
Output: 2
```
 

## Constraints

- `1 <= nums.length <= 10^4`
- `0 <= nums[i] <= 1000`
- It's guaranteed that you can reach `nums[n - 1]`.

---

## Approach 1: Greedy

### Intuition

We can use a greedy approach to solve this problem. 
We keep track of the farthest index we can reach from the current index. 
We also keep track of the end of the current jump. 
When we reach the end of the current jump, we increment the number of jumps and update the end of the current jump to the farthest index we can reach.

### Complexity Analysis

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

---

## Approach 2: Dynamic Programming

### Intuition

We can use dynamic programming to solve this problem. 
We define `dp[i]` as the minimum number of jumps to reach index `i`. 
We can initialize `dp[0]` as 0. 
For each index `i`, we can iterate over all indices `j` where `j + nums[j] >= i` and update `dp[i]` as `min(dp[i], dp[j] + 1)`.

### Complexity Analysis

- **Time Complexity:** `O(n^2)`
- **Space Complexity:** `O(n)`

---

## Implementation

See `solution.py` for the full implementation.
