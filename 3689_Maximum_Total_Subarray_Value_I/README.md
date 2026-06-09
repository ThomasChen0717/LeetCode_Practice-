# 3689. Maximum Total Subarray Value I

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Array, Greedy  

---

## Problem Description

You are given an integer array `nums` of length `n` and an integer `k`.

You need to choose **exactly** `k` non-empty `nums[l..r]` of `nums`. Subarrays may overlap, and the exact same subarray (same `l` and `r`) **can** be chosen more than once.

The **value** of a subarray `nums[l..r]` is defined as: `max(nums[l..r]) - min(nums[l..r])`.

The **total value** is the sum of the **values** of all chosen subarrays.

Return the **maximum** possible total value you can achieve.

---

## Examples
**Example 1:**
```
Input: nums = [1,3,2], k = 2
Output: 4
```
**Example 2:**
```
Input: nums = [4,2,5,1], k = 3
Output: 12
```

## Constraints

- `1 <= n == nums.length <= 5 * 10​​​​​​​4`
- `0 <= nums[i] <= 10^9`
- `1 <= k <= 10^5`

---

## Approach

### Intuition

The problem asks us to find the maximum total value by choosing `k` subarrays. The value of a subarray is the difference between its maximum and minimum element. A crucial detail is that we can choose the same subarray multiple times.

This suggests a greedy approach. To maximize the total sum, we should try to maximize the value of each of the `k` chosen subarrays.  Let's consider what the maximum possible value of a single subarray can be. The value is `max(sub) - min(sub)`. To maximize this difference, we need the largest possible `max` and the smallest possible `min`.

The global maximum and global minimum of the entire `nums` array will give the largest possible difference. Any subarray will have a maximum that is less than or equal to the global maximum and a minimum that is greater than or equal to the global minimum. Therefore, the maximum possible value for any subarray is `max(nums) - min(nums)`.

Since we can repeat subarrays, the optimal strategy is to find the single subarray that yields the highest value and select it `k` times. The subarray containing both the global minimum and global maximum of the `nums` array will have this maximum possible value.

Thus, the problem simplifies to:
1. Find the minimum (`min_val`) and maximum (`max_val`) elements in the entire `nums` array.
2. The maximum value for a single subarray is `max_val - min_val`.
3. Since we choose `k` subarrays, the maximum total value is `(max_val - min_val) * k`.

### Complexity Analysis

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

---

## Implementation

See `solution.c++` for the full implementation.
