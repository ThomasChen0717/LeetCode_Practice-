# 1877. Minimize Maximum Pair Sum in Array

**Difficulty:** <span style="color:#f0ad4e"><b>Medium</b></span>  
**Topics:** Arrays, Sorting

---

## Problem Description

The `pair sum` of a pair `(a,b)` is equal to `a + b`. The **maximum pair sum** is the largest **pair sum** in a list of pairs.

- For example, if we have pairs `(1,5)`, `(2,3)`, and `(4,4)`, the maximum pair sum would be `max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8`.

Given an array `nums` of even length `n`, pair up the elements of `nums` into `n / 2` pairs such that:

  - Each element of `nums` is in **exactly one** pair, and
  - The **maximum pair sum** is **minimized.**

Return the minimized **maximum pair sum** after optimally pairing up the elements.

---

## Examples
Example 1:
```
Input: nums = [3,5,2,3]
Output: 7
Explanation: The elements can be paired up into pairs (3,3) and (5,2).
The maximum pair sum is max(3+3, 5+2) = max(6, 7) = 7.
```
Example 2:
```
Input: nums = [3,5,4,2,4,6]
Output: 8
Explanation: The elements can be paired up into pairs (3,5), (4,4), and (6,2).
The maximum pair sum is max(3+5, 4+4, 6+2) = max(8, 8, 8) = 8.
```
## Constraints

- `n == nums.length`
- `2 <= n <= 10^5`
- `n` is **even**.
- `1 <= nums[i] <= 10^5`

---

## Approach: Sorting 

### Intuition

Sort the array then pair the smallest with the Largest.

### Complexity Analysis

- **Time Complexity:** `O(n log n)` due to sorting.
- **Space Complexity:** `O(log n)` or `O(n)` depending on the sorting algorithm.

---

## Implementation

See `solution.py` for the full implementation.
