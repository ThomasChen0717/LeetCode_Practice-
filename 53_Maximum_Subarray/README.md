# 53. Maximum Subarray

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Array, Dynamic Programming, Divide and Conquer

---

## Problem Description

Given an integer array `nums`, find the subarray with the largest sum, and return its sum.

---

## Examples
Example 1:
```
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
```
Example 2:
```
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
```
Example 3:
```
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
```

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

---

## Approach 1: Optimized Brute Force

### Intuition

Iterate through all possible subarrays and keep track of the maximum sum. The optimization is that we only need to keep track of the current sum at each `i` and the maximum sum. We can update the current sum by adding the current element to it. 

### Complexity Analysis

- **Time Complexity:** `O(n^2)`
- **Space Complexity:** `O(1)` 

---

## Approach 2: Dynamic Programming, Kadane's Algorithm

### Intuition

We can traverse the array, keeping a current sum of the subarray ending at the current index. If the current sum is negative, we can throw it away because it will only decrease the sum of any future subarray. Otherwise, we can keep adding to it. The maximum sum of a subarray ending at index `i` is either the current element itself or the current element plus the maximum sum of a subarray ending at index `i-1`.

### Complexity Analysis

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)` 

---

## Approach 3: Divide and Conquer

### Intuition

We can divide the array into two halves. The maximum sum of a subarray crossing the middle element is the middle element plus the maximum sum on the left and right subarrays. Then we recursively calculate the maximum sum of left and right halves. The maximum sum is then the max of the three sums. 

### Complexity Analysis

- **Time Complexity:** `O(n log n)`
- **Space Complexity:** `O(log n)` 

---

## Implementation

See `solution.py` for the full implementation.
