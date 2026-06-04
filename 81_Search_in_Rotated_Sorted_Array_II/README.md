# 81. Search in Rotated Sorted Array II

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Array, Binary Search

---

## Problem Description

There is an integer array `nums` sorted in non-decreasing order (not necessarily with **distinct** values).

Before being passed to your function, `nums` is **rotated** at an unknown pivot index `k` (`0 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (**0-indexed**). For example, `[0,1,2,4,4,4,5,6,6,7]` might be rotated at pivot index `5` and become `[4,5,6,6,7,0,1,2,4,4]`.

Given the array `nums` **after** the rotation and an integer `target`, return `true` if `target` is in `nums`, or `false` if it is not in `nums`.

You must decrease the overall operation steps as much as possible.

---

## Examples

**Example 1:**
```
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
```

**Example 2:**
```
Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
```

## Constraints

- `1 <= nums.length <= 5000`
- `-10^4 <= nums[i] <= 10^4`
- `nums` is guaranteed to be rotated at some pivot.
- `-10^4 <= target <= 10^4`

---

## Approach: Binary Search with Duplicate Handling

### Intuition

This problem is a follow-up to "Search in Rotated Sorted Array I," with the added complexity that the array can contain duplicate elements. The core idea is still to use a modified binary search, but the presence of duplicates introduces a tricky edge case.

In a standard rotated array search, we can always determine which half of the array (from `left` to `mid` or `mid` to `right`) is sorted by comparing `nums[mid]` with `nums[left]` or `nums[right]`. However, if `nums[left]`, `nums[mid]`, and `nums[right]` are all equal, we can't determine which half is sorted. For example, in an array like `[1, 0, 1, 1, 1]`, if `left=0`, `right=4`, and `mid=2`, then `nums[left] == nums[mid] == nums[right] == 1`. In this situation, the pivot (0) could be in either the left or the right half.

To handle this ambiguity, when we encounter the case `nums[left] == nums[mid] == nums[right]`, we can't make an intelligent decision to discard one half of the search space. The safest move is to simply shrink our search window from left(since we compare with leftmost element) by incrementing `left`. This might degrade the performance to linear time in the worst case (e.g., an array of all the same elements), but on average, it allows the binary search to proceed.

For all other cases (where `nums[left]`, `nums[mid]`, and `nums[right]` are not all equal), the logic is similar to the original problem:
1.  If `nums[mid] == target`, we found it.
2.  If the left half (`nums[left]` to `nums[mid]`) is sorted (`nums[left] <= nums[mid]`):
    - Check if the `target` lies within this sorted half. If so, search left (`right = mid - 1`).
    - Otherwise, search right (`left = mid + 1`).
3.  If the right half (`nums[mid]` to `nums[right]`) is sorted (`nums[mid] < nums[left]`):
    - Check if the `target` lies within this sorted half. If so, search right (`left = mid + 1`).
    - Otherwise, search left (`right = mid - 1`).

By adding the special handling for duplicates, we can correctly search the array.

### Complexity Analysis

- **Time Complexity:** `O(log N)` on average, but `O(N)` in the worst case. The worst case occurs when all elements are the same, and we have to shrink the search window one element at a time from both ends.
- **Space Complexity:** `O(1)`. We only use a few variables for pointers, which is constant extra space.

---

## Implementation

See `solution.c++` for the full implementation.
