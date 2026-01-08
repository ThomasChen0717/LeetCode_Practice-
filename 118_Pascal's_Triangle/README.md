# 118. Pascal's Triangle

**Difficulty:** <span style="color:#2ecc71"><b>Easy</b></span>  
**Topics:** Dynamic Programming, Array

---

## Problem Description
Given an integer `numRows`, return the first numRows of **Pascal's triangle**.

In **Pascal's triangle**, each number is the sum of the two numbers directly above it.

---

## Examples
Example 1:
```
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
```
Example 2:
```
Input: numRows = 1
Output: [[1]]
```
## Constraints

- `1 <= numRows <= 30`

---

## Approach: Dynamic Programming (DP)

### Intuition
Each row of Pascal's triangle is generated based on the previous row. The first row is always [1]. For each subsequent row, the first and last elements are always 1. The middle elements are the sum of the two elements directly above them in the previous row.

### Complexity Analysis
Let `n` be the number of rows.
- **Time Complexity:** `O(n^2)`
- **Space Complexity:** `O(1)`

---

## Implementation

See `solution.py` for the full implementation.
