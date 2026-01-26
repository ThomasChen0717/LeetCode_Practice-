# 215. Kth Largest Element in an Array

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Heap, Quick Select, Counting Sort

---

## Problem Description

Given an integer array `nums` and an integer `k`, return the `kth` largest element in the array.

Note that it is the `kth` largest element in the sorted order, not the `kth` distinct element.

Can you solve it without sorting?

---

## Examples
Example 1:
```
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
```
Example 2:
```
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
```

## Constraints

- `1 <= k <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

---

## Approach 1: Sorting

### Intuition

Sort the array in descending order. The `kth` largest element will be at index `k-1`.


### Complexity Analysis

- **Time Complexity:** `O(n log n)`
- **Space Complexity:** `O(n)` or `O(log n)` depending on the coding language.

---

## Approach 2: Min Heap

### Intuition

Use a min heap to keep track of the `k` largest elements seen so far. The top element of the heap will be the `kth` largest element.

### Complexity Analysis

- **Time Complexity:** `O(n log k)`
- **Space Complexity:** `O(k)`

--- 

## Approach 3: Quick Select

### Intuition

Use the Quick Select algorithm to find the `kth` largest element. The algorithm works by partitioning the array around a pivot element. We keep all elements larger than the pivot element in the left partition. We keep all elements smaller than the pivot element in the right partition. If the left partition has greater than or equal to `k` elements, then the `kth` largest element is in the left partition. If the left partition plus the pivot elements are less than `k`, then the `kth` largest element is in the right partition. If we find that the target is not in left or right partition, then we have found it at the pivot. We do this process repeatedly. 

### Complexity Analysis

- **Time Complexity:** `O(n)` on average, `O(n^2)` in the worst case.
- **Space Complexity:** `O(n)`

--- 

## Approach 4: Counting Sort

### Intuition

Use the Counting Sort algorithm to find the `kth` largest element. The algorithm works by counting the number of occurrences of each element in the array. We then iterate through the counts to find the `kth` largest element. 

We use a `maxValue` and a `minValue` to determine the range of the array. We then create a count array of size `maxValue - minValue + 1`. We iterate through the array and increment the count of each element. We then iterate through the count array to find the `kth` largest element.

### Complexity Analysis
Let `n` be the length of the array and `m` be `maxValue - minValue`. 
- **Time Complexity:** `O(n + m)`
- **Space Complexity:** `O(m)`

## Implementation

See `solution.py` for the full implementation.
