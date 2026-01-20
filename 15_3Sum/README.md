# 3Sum

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Arrays, Two Pointers, Sorting, Hash Table, Hash Set

---

## Problem Description

Given an integer array nums, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

---

## Examples
Example 1:
```
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
```
Example 2:
```
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
```
Example 3:
```
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
```

## Constraints

- `3 <= nums.length <= 3000`
- `-10^5 <= nums[i] <= 10^5`

---

## Approach 1: Sorting and Two Pointers

### Intuition

First sort the array. Then we iterate through the array, and for each element `nums[i]`, we use two pointers on `nums[i+1:]` to find the other two elements that sum up to `-nums[i]`. 
If the sum is less than zero, we move the left pointer to the right. If the sum is greater than zero, we move the right pointer to the left. If the sum is zero, we add the triplet to the result. 

We need to skip the duplicate elements to avoid duplicate triplets both when iterating through the array and when moving the pointers. 

### Complexity Analysis

- **Time Complexity:** `O(n^2)`
- **Space Complexity:** `O(log n)` to `O(n)` depending on the sorting algorithm.

---

## Approach 2: Sorting with Hash Set

### Intuition

First sort the array. Then we iterate through the array, and for each element `nums[i]`, we use a hash set to find the other two elements in the range `nums[i+1:]` that sum up to `-nums[i]`. 
If the sum is zero, we add the triplet to the result. 

We need to skip the duplicate elements to avoid duplicate triplets both when iterating through the array and when moving the pointer.

### Complexity Analysis

- **Time Complexity:** `O(n^2)`
- **Space Complexity:** `O(n)`

---

## Approach 3: Hash with Triplet Sorting for Duplicate Elimination

### Intuition

We use a hash set to store the triplets. For each element `nums[i]`, we use a hash set to find the other two elements in the range `nums[i+1:]` that sum up to `-nums[i]`. 
If the sum is zero, we add the triplet to the hash set. 
After iterating through the array, we sort the hash set and convert it to a list of lists.
The hash set should be sorted by the elements in each triplet to avoid duplicate triplets. 

Use a `dup` hashset to avoid duplicate elements in the outer loop.
Use a `seen` hashset to avoid duplicate elements in the inner loop. 


### Complexity Analysis

- **Time Complexity:** `O(n^2)`
- **Space Complexity:** `O(n)`

---

## Implementation

See `solution.py` for the full implementation.
