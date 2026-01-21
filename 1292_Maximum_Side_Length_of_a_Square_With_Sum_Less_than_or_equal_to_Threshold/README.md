# 1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Binary Search, Prefix Sum, Matrix

---

## Problem Description

Given a `m x n` matrix `mat` and an integer `threshold`, return the maximum side-length of a square with a sum less than or equal to `threshold` or return `0` if there is no such square.

---

## Examples
Example 1:
![Example 1](https://assets.leetcode.com/uploads/2019/12/05/e1.png)
```
Input: mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
Output: 2
Explanation: The maximum side length of square with sum less than 4 is 2 as shown.
```
Example 2:
```
Input: mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1
Output: 0
```

## Constraints

- `m == mat.length`
- `n == mat[i].length`
- `1 <= m, n <= 300`
- `0 <= mat[i][j] <= 10^4`
- `0 <= threshold <= 10^5`

---

## Approach 1: Binary Search + Prefix Sum

### Intuition

First we compute the prefix sum matrix `prefix_sum` where `prefix_sum[i][j]` is the sum of the elements in the rectangle from `(1, 1)` to `(i, j)`. 

Then we can use binary search to find the maximum side length of the square. For each side length `k`, we check if there is a square of side length `k` with sum less than or equal to `threshold`. 

### Complexity Analysis

- **Time Complexity:** `O(M * N * log(min(M, N)))`
- **Space Complexity:** `O(M * N)`

---

## Approach 2: Optimized Enumeration + Prefix Sum

### Intuition

First we compute the prefix sum matrix `prefix_sum` where `prefix_sum[i][j]` is the sum of the elements in the rectangle from `(1, 1)` to `(i, j)`. 

Then we can enumerate all possible squares of side length `k` and check if their sum is less than or equal to `threshold`. With two optimization techniques:
- Since all elements in `mat` are non-negative, once the sum of a square with side length `c` exceeds the threshold, any larger square with the same top-left corner will also exceed the threshold. Therefore, we can stop increasing `c` immediately.
- If we have already found a valid square with side length `c'`, then for any subsequent top-left corner `(i, j)`, there is no need to check side lengths less than or equal to `c'`. We can start directly from `c' + 1`.

### Complexity Analysis

- **Time Complexity:** `O(M * N)`
- **Space Complexity:** `O(M * N)`

---

## Implementation

See `solution.py` for the full implementation.
