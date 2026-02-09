# 347. Top K Frequent Elements

**Difficulty:** <span style="color:#2ecc71"><b>Medium</b></span>  
**Topics:** Hash Table, Heap, Quick Select

---

## Problem Description

Given an integer array `nums` and an integer `k`, return *the `k` most frequent elements.* You may return the answer in **any order**.

---

## Examples

Example 1:
```
Input: nums = [1,1,1,2,2,3], k = 2

Output: [1,2]
```
Example 2:
```
Input: nums = [1], k = 1

Output: [1]
```
Example 3:
```
Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

Output: [1,2]
```

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `k` is in the range `[1, the number of unique elements in the array]`.
- It is **guaranteed** that the answer is **unique**.

---

## Approach 1: Hash Map + Heap

### Intuition

1. Use a hash map to count the frequency of each element in `nums`.
2. Use a heap to keep track of the `k` most frequent elements.
3. Return the elements in the heap.

### Complexity Analysis
Let `n` be the length of `nums`.
- **Time Complexity:** `O(n log k)`
- **Space Complexity:** `O(n + k)`

---

## Approach 2: Quick Select

### Intuition

1. Use a hash map to count the frequency of each element in `nums`.
2. Use Quick Select to find the `n-k`th least frequent element.
    - Partition the array based on the frequency of elements.
    - If the pivot index is equal to `n-k`, return the pivot element.
    - If the pivot index is greater than `n-k`, recursively search the left subarray.
    - If the pivot index is less than `n-k`, recursively search the right subarray.
3. Return the elements with frequency greater than or equal to the `n-k`th least frequent element.

### Complexity Analysis
Let `n` be the length of `nums`.
- **Time Complexity:** `O(n)` on average, `O(n^2)` in the worst case.
- **Space Complexity:** `O(n)`

---

## Implementation

See `solution.py` for the full implementation.
