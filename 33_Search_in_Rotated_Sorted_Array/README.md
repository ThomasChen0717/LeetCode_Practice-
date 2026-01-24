# 33. Search in Rotated Sorted Array

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Binary Search, Array

---

## Problem Description

There is an integer array `nums` sorted in ascending order (with **distinct** values).

Prior to being passed to your function, `nums` is **possibly left rotated** at an unknown index `k` (`1 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (**0-indexed**). For example, `[0,1,2,4,5,6,7]` might be left rotated by `3` indices and become `[4,5,6,7,0,1,2]`.

Given the array `nums` **after** the possible rotation and an integer `target`, return the index of `target` if it is in `nums`, or `-1` if it is not in `nums`.

You must write an algorithm with `O(log n)` runtime complexity.

---

## Examples
Example 1:
```
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
```
Example 2:
```
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```
Example 3:
```
Input: nums = [1], target = 0
Output: -1
```

## Constraints

- `1 <= nums.length <= 5000`
- `-10^4 <= nums[i] <= 10^4`
- All values of `nums` are **unique**.
- `nums` is an ascending array that is possibly rotated.
- `-10^4 <= target <= 10^4`

---

## Approach 1: Binary Search to find the pivot index and two binary searches on the two sorted halves

### Intuition

First we find the pivot index `pivot` where the array is rotated. Then we can divide the array into two sorted halves: `nums[0:pivot+1]` and `nums[pivot+1:]`. We can then perform binary search on each half to find the target.

### Complexity Analysis

- **Time Complexity:** `O(log n)`
- **Space Complexity:** `O(1)`

---

## Approach 2: Binary Search to find pivot index and then use index shift to find target

### Intuition

First we find the pivot index `pivot` where the array is rotated. Then we can shift the index of the target by `pivot` to do binary search to find the target in the original array.

### Complexity Analysis

- **Time Complexity:** `O(log n)`
- **Space Complexity:** `O(1)`

---

## Approach 3: Single Binary Search

### Intuition

We can perform a single binary search to find the target. The key is to adjust the mid index to account for the rotation. If `nums[mid] >= nums[left]`, then the left half is sorted. Otherwise, the right half is sorted. We can then check if the target is in the sorted half or the other half.

### Complexity Analysis

- **Time Complexity:** `O(log n)`
- **Space Complexity:** `O(1)`

---

## Implementation

See `solution.py` for the full implementation.
