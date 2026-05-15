# 153. Find Minimum in Rotated Sorted Array

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Array, Binary Search

---

## Problem Description

Suppose an array of length `n` sorted in ascending order is rotated between 1 and `n` times. For example, the array `nums = [0,1,2,4,5,6,7]` might become:
- `[4,5,6,7,0,1,2]` if it was rotated 4 times.
- `[0,1,2,4,5,6,7]` if it was rotated 7 times.

Notice that rotating an array `[a[0], a[1], a[2], ..., a[n-1]]` 1 time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.

Given the sorted rotated array `nums` of **unique** elements, return the minimum element of this array.

You must write an algorithm that runs in `O(log n)` time.

---

## Examples

**Example 1:**
```
Input: nums = [3,4,5,1,2]
Output: 1
```
**Explanation:** The original array was `[1,2,3,4,5]` rotated 3 times.

**Example 2:**
```
Input: nums = [4,5,6,7,0,1,2]
Output: 0
```
**Explanation:** The original array was `[0,1,2,4,5,6,7]` and it was rotated 4 times.

**Example 3:**
```
Input: nums = [11,13,15,17]
Output: 11
```
**Explanation:** The original array was `[11,13,15,17]` and it was rotated 4 times.

## Constraints

- `n == nums.length`
- `1 <= n <= 5000`
- `-5000 <= nums[i] <= 5000`
- All the integers of `nums` are **unique**.
- `nums` is sorted and rotated between 1 and `n` times.

---

## Approach: Binary Search

### Intuition

The problem requires finding the minimum element in a rotated sorted array in `O(log n)` time, which strongly suggests using binary search. A rotated sorted array consists of two sorted portions. The minimum element is the pivot point where the rotation occurs—it's the first element of the second sorted portion.

The key is to identify which part of the array contains this pivot point.

1.  **Handle the non-rotated case:** First, we can check if the array is not rotated at all (or rotated `n` times). This is true if `nums[0] <= nums[n-1]`. In this case, the minimum element is simply `nums[0]`.

2.  **Binary Search for the pivot:** If the array is rotated, the minimum element will be the only element that is smaller than its previous element. We can use binary search to find this inflection point.
    - We initialize `left` and `right` pointers to the start and end of the array.
    - In each step, we calculate `mid`. We then check if `nums[mid]` is the pivot:
        - If `nums[mid] > nums[mid + 1]`, then `nums[mid + 1]` is the smallest element.
        - If `nums[mid - 1] > nums[mid]`, then `nums[mid]` is the smallest element.
    - If `mid` is not the pivot, we need to decide which half to search next. We can compare `nums[mid]` with `nums[0]`. 
        - If `nums[mid] > nums[0]`, it means the elements from `0` to `mid` are in the first, larger part of the rotated array. The pivot must be in the right half, so we set `left = mid + 1`.
        - If `nums[mid] < nums[0]`, it means `mid` is in the second, smaller part of the array. The pivot could be `nums[mid]` or in the left half, so we set `right = mid - 1`.

By repeatedly narrowing the search space, we can find the minimum element efficiently.

### Complexity Analysis

- **Time Complexity:** `O(log N)`, where `N` is the number of elements in `nums`. This is because binary search halves the search space in each iteration.
- **Space Complexity:** `O(1)`. We only use a few variables to keep track of pointers, which is constant extra space.

---

## Implementation

See `solution.py` for the full implementation.
