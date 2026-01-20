# 198. House Robber

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Dynamic Programming, Recursion, Memoization

---

## Problem Description

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and **it will automatically contact the police if two adjacent houses were broken into on the same night**.

Given an integer array `nums` representing the amount of money of each house, return the maximum amount of money you can rob tonight **without alerting the police.**

---

## Examples
Example 1:
```
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
```
Example 2:
```
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
```

## Constraints

- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 400`

---

## Approach 1: Top-Down Recursive with Memoization

### Intuition

We can use a recursive approach to solve this problem. For each house, we have two options: rob it or not rob it. If we rob the current house, we cannot rob the next house. If we do not rob the current house, we can rob the next house. We can use memoization to avoid recalculating the maximum amount of money that can be robbed from the houses starting from a particular index.

### Complexity Analysis
Let `n` be the length of the input array `nums`.
- **Time Complexity:** `O(n)`.
- **Space Complexity:** `O(n)`

---

## Approach 2: Bottom-Up Dynamic Programming

### Intuition

We can use a bottom-up approach to solve this problem. We can create a dp array where `dp[i]` represents the maximum amount of money that can be robbed from the houses ending on index `i`(inclusive). We can initialize `dp[0]` to `nums[0]` and `dp[1]` to `max(nums[0], nums[1])`. We can then iterate from `2` to `n-1` and for each index `i`, we can calculate `dp[i]` as `max(nums[i] + dp[i-2], dp[i-1])`. We return `dp[n-1]`.

### Complexity Analysis
- **Time Complexity:** `O(n)`.
- **Space Complexity:** `O(n)`

---

## Approach 3: Bottom-Up Dynamic Programming with Constant Space

### Intuition

We can use a bottom-up approach to solve this problem with constant space. We can use two variables `rob` and `rob_skip` to keep track of the maximum amount of money that can be robbed from the houses ending on index `i-1` and `i-2` respectively. We can initialize `rob` to `nums[0]` and `rob_skip` to `0`. We can then iterate from `1` to `n-1` and for each index `i`, we can calculate `rob` as `max(nums[i] + rob_skip, rob)` and update `rob_skip` to `rob`. We return `rob`.

### Complexity Analysis
- **Time Complexity:** `O(n)`.
- **Space Complexity:** `O(1)`

---

## Implementation

See `solution.py` for the full implementation.
