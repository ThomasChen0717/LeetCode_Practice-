# 3634. Minimum Removals to Balance Array

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Sorting, Two Pointers

---

## Problem Description

You are given an integer array `nums` and an integer `k`.

An array is considered **balanced** if the value of its **maximum** element is at most `k` times the **minimum** element.

You may remove **any** number of elements from `nums​​​​​​​` without making it **empty**.

Return the **minimum** number of elements to remove so that the remaining array is balanced.

**Note:** An array of size 1 is considered balanced as its maximum and minimum are equal, and the condition always holds true.
---

## Examples
Example 1:
```
Input: nums = [2,1,5], k = 2

Output: 1

Explanation:
Remove nums[2] = 5 to get nums = [2, 1].
Now max = 2, min = 1 and max <= min * k as 2 <= 1 * 2. Thus, the answer is 1.
```
Example 2:
```
Input: nums = [1,6,2,9], k = 3

Output: 2

Explanation:

Remove nums[0] = 1 and nums[3] = 9 to get nums = [6, 2].
Now max = 6, min = 2 and max <= min * k as 6 <= 2 * 3. Thus, the answer is 2.
```
Example 3:
```
Input: nums = [4,6], k = 2

Output: 0

Explanation:

Since nums is already balanced as 6 <= 4 * 2, no elements need to be removed.
```
## Constraints

- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`
- `1 <= k <= 10^5`

---

## Approach: Sorting + Two Pointers

### Intuition

We first sort the array `nums`. Then, we use two pointers `left` and `right` to find the minimum number of elements to remove. Both pointers start at the beginning of the array. We move the `right` pointer to the right until `nums[right] > nums[left] * k`. Then, we update the minimum number of elements to remove as `n - (right - left)`. We move the `left` pointer to the right and repeat the process until `left` reaches the end of the array.

### Complexity Analysis

- **Time Complexity:** `O(n log n)`
- **Space Complexity:** `O(log n)` or `O(n)` depending on the sorting algorithm.

---

## Implementation

See `solution.py` for the full implementation.
