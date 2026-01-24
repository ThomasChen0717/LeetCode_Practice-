# 78. Subsets

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Array, Backtracking, Bitmasking

---

## Problem Description

Given an integer array `nums` of **unique** elements, return all possible subsets (the power set).

The solution set **must not** contain duplicate subsets. Return the solution in **any order**.

---

## Examples
Example 1:
```
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
```
Example 2:
```
Input: nums = [0]
Output: [[],[0]]
```

## Constraints

- `1 <= nums.length <= 10`
- `-10 <= nums[i] <= 10`
- All the integers of `nums` are **unique**.

---

## Approach 1: Cascading

### Intuition

We can think of the cascading approach as a process of adding each element to all existing subsets. 
For example, if we have the subsets `[[],[1],[2],[1,2]]` and we want to add `3`, we would get `[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]`.

### Complexity Analysis

- **Time Complexity:** `O(N * 2^N)`
- **Space Complexity:** `O(N * 2^N)`

---

## Approach 2: Backtracking

### Intuition

We can use backtracking to generate all possible subsets. 
We keep a index `idx` to keep track of the current element we are considering. 
At each step, we have two choices: either include the current element in the subset or exclude it. 
We recursively call the backtracking function with the updated subset and index.

### Complexity Analysis

- **Time Complexity:** `O(N * 2^N)`
- **Space Complexity:** `O(N)`

---
## Approach 3: Bitmasking

### Intuition

We can use bitmasking to generate all possible subsets. 
We use a binary number of length `n` to represent whether each element is included in the subset. 
For example, if `n = 3`, we have `000`, `001`, `010`, `011`, `100`, `101`, `110`, `111` as possible bitmasks.

### Complexity Analysis

- **Time Complexity:** `O(N * 2^N)`
- **Space Complexity:** `O(N)`

---

## Implementation

See `solution.py` for the full implementation.
