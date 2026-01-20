# 540. Single Element in a Sorted Array

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Array, Binary Search

---

## Problem Description

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in `O(log n)` time and `O(1)` space.

---

## Examples
Example 1:
```
Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
```
Example 2:
```
Input: nums = [3,3,7,7,10,11,11]
Output: 10
```

## Constraints

- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^5`

---

## Approach 1: Brute Force

### Intuition

Search for the single element in the array by iterating through the array and checking if the current element is equal to the previous element. If not, return the previous element. Increment in steps of 2.

### Complexity Analysis

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

---

## Approach 2: Binary Search

### Intuition

We can use binary search to find the single element in the array. 
We keep track of the parity of the left and right subarray length. 
After removing the mid elements, one of the subarrays must have an odd length. 
We can then update the search space to the odd subarray. 

### Complexity Analysis

- **Time Complexity:** `O(log n)`
- **Space Complexity:** `O(1)`

---

## Approach 3: Binary Search on Even Indexes

### Intuition

We can use binary search only on even indexes. 
If the mid index is odd, we can decrement it by 1. 
We can then check if the mid element is equal to the next element. 
Because any pair to the right of the single element will have the first element of the pair on an odd index and any pair to the left of the single element will have the first element of the pair on an even index. 
We can then update the search space accordingly.

### Complexity Analysis

- **Time Complexity:** `O(log n)`
- **Space Complexity:** `O(1)`

---

## Implementation

See `solution.py` for the full implementation.
