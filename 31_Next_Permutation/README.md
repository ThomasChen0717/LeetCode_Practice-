# 31. Next Permutation

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Array, Math

---

## Problem Description

A **permutation** of an array of integers is an arrangement of its members into a sequence or linear order.

- For example, for `arr = [1,2,3]`, the following are all the permutations of `arr`: `[1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1]`.

The **next permutation** of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the **next permutation** of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

- For example, the next permutation of `arr = [1,2,3]` is `[1,3,2]`.
- Similarly, the next permutation of `arr = [2,3,1]` is `[3,1,2]`.
- While the next permutation of `arr = [3,2,1]` is `[1,2,3]` because `[3,2,1]` does not have a lexicographical larger rearrangement.

Given an array of integers `nums`, find the next permutation of `nums`.

The replacement must be in place and use only constant extra memory.

---

## Examples
Example 1:
```
Input: nums = [1,2,3]
Output: [1,3,2]
```
Example 2:
```
Input: nums = [3,2,1]
Output: [1,2,3]
```
Example 3:
```
Input: nums = [1,1,5]
Output: [1,5,1]
```

## Constraints

- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 100`

---

## Approach: Single Pass

### Intuition

Observe that for any given sequence that is in descending order, no next larger permutation is possible. 

To find the next smallest permutation, we need to find the first pair of adjacent elements `(i, i+1)` from the right such that `nums[i] < nums[i+1]`. This element `nums[i]` is the pivot that we will swap to find the next permutation. 

We then iterate the right of the pivot to find the smallest element `nums[j]` that is greater than `nums[i]`. This element `nums[j]` will be the new pivot that we will swap with `nums[i]`. 

After swapping `nums[i]` and `nums[j]`, we reverse the subarray to the right of `i` to ensure the next smallest permutation.

### Complexity Analysis

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

---

## Implementation

See `solution.py` for the full implementation.
