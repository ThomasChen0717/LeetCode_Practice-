# 85. Maximal Rectangle

**Difficulty:** <span style="color:#e74c3c"><b>Hard</b></span>  
**Topics:** Dynamic Programming, Stack

---

## Problem Description

Given a `rows x cols` binary `matrix` filled with `0`'s and `1`'s, find the largest rectangle containing only `1`'s and return its area.

---

## Examples
Example 1:
![Example 1](https://assets.leetcode.com/uploads/2020/09/14/maximal.jpg)
```
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.
```
Example 2:
```
Input: matrix = [["0"]]
Output: 0
```
Example 3:
```
Input: matrix = [["1"]]
Output: 1
```

## Constraints

- `rows == matrix.length`
- `cols == matrix[i].length`
- `1 <= rows, cols <= 200`
- `matrix[i][j]` is `'0'` or `'1'`.

---

## Approach 1: Dynamic Programming

### Intuition

Use a 2D array `dp` where `dp[i][j]` represents the width of the line ending at `matrix[i][j]`.

Then, for each of the point, we can calculate the min width that is shared across the entire vertical slap(different rows) ending at this point. 

Calculate the max area for each point, and update the max area. 


### Complexity Analysis
Let `N` be the number of rows, and `M` be the number of columns.
- **Time Complexity:** `O(N^2M)`
    - Computing max area for each point: `O(N)` since it iterates each column 
    - Iterated over each point: `O(NM)` 
- **Space Complexity:** `O(NM)`
    - `dp` array: `O(NM)`

---

# Approach 2: Using Stack for Histogram area 

Similar to approach 1, but instead of keeping a 2D array `dp`, we use a 1D array `dp` to keep the height of the current point.

Then for each row, we use the histogram area approach in leetcode 84 to calculate the max area for this row. 

### Complexity Analysis
- **Time Complexity:** `O(NM)`
    - Iterated over each cell: `O(NM)`
    - For each row, we calculate the max area using the histogram area approach: `O(M)`
- **Space Complexity:** `O(M)`
    - `dp` array: `O(M)`
    - Stack: `O(M)`

## Approach 3: Dynamic Programming - Maximum Height at Each Point 

### Intuition

Use three arrays of size `n` to keep the maximum height, left boundary, and right boundary for each point. 

For each cell, we update the maximum height from the previous value if the cell is `1`. Otherwise, we reset the height to `0`.

We also update the left boundary if the cell is `1`. Otherwise, we set the left boundary to `0`.

The right boundary is updated in a similar way. Note right is maintained so that it is one more than the rightmost `1` in the current row.

Finally, for each cell, we calculate the max area using the formula `height * (right - left)`.


### Complexity Analysis
- **Time Complexity:** `O(NM)`
    - In each iteration over `N`, we iterate over `M` a constant number of times.
- **Space Complexity:** `O(M)`
    - arrays `height`, `left`, and `right` each have size `M`. 

## Implementation

See `solution.py` for the full implementation.
