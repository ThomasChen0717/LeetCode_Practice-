# 48. Rotate Image 

**Difficulty:** <span style="color:#f"><b>Medium</b></span>  
**Topics:** Matrix, Math

---

## Problem Description

You are given an `n x n` 2D `matrix` representing an image, rotate the image by **90** degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. **DO NOT** allocate another 2D matrix and do the rotation.

---

## Examples
Example 1:
![Image](https://assets.leetcode.com/uploads/2020/08/28/mat1.jpg)
```
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
```
Example 2:
![Image](https://assets.leetcode.com/uploads/2020/08/28/mat2.jpg)
```
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
```

## Constraints

- `n == matrix.length == matrix[i].length`
- `1 <= n <= 20`
- `1000 <= matrix[i][j] <= 1000`

---

## Approach 1: Rotate Four Elements at a time

### Intuition

We can iterate over each group of four cells and rotate them.

Notice for a cell `(i,j)` , its rotated position is `(j,n-i-1)`, where `n` is the size of the matrix. We can rotate the four cells in a group in a single pass. 

We iterate over two loops:
- The outer loop iterates over the first half of the rows. 
    - Add 1 if `n` is odd.
- The inner loop iterates over half of the columns in the current row.  


### Complexity Analysis
Let `m` be the size of the matrix.
- **Time Complexity:** `O(m)`
- **Space Complexity:** `O(1)`

---

## Approach 2: Transpose and Reflect

### Intuition

We can rotate the matrix by transposing it and then reflecting it.

### Complexity Analysis
- **Time Complexity:** `O(m)`
- **Space Complexity:** `O(1)`

--- 

## Implementation

See `solution.py` for the full implementation.
