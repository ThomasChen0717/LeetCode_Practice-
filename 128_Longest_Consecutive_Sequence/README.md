# 128 Longest Consecutive Sequence

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** HashSet, Sorting, Array

---

## Problem Description

Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in `O(n)` time.

---

## Examples
Example 1:
```
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
```
Example 2:
```
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
```
Example 3:
```
Input: nums = [1,0,1,2]
Output: 3
 ```


## Constraints

- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

---

## Approach 1: Brute Force

### Intuition

For each number in the array, we try to find if the consecutive numbers exist in the array. 
If they do, we update the longest consecutive sequence accordingly.

### Complexity Analysis

- **Time Complexity:** `O(n^3)`
- **Space Complexity:** `O(1)`

---

## Approach 2: Sorting

### Intuition

We can sort the array and then find the longest consecutive sequence.
Remember to skip the duplicates.

### Complexity Analysis

- **Time Complexity:** `O(nlogn)`
- **Space Complexity:** `O(n)` or `O(log n)` depending on the sorting algorithm.

---

## Approach 3: Brute Force with HashSet

### Intuition

We can use a HashSet to store the numbers in the array.
Then, for each number, we first check if the number minus one is in the HashSet. This means that the number is not the start of a consecutive sequence. 
If it is not, we try to find if the consecutive numbers exist in the HashSet and record the length of the consecutive sequence.


### Complexity Analysis

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

---

## Implementation

See `solution.py` for the full implementation.
