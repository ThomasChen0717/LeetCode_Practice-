# 1975. Maximum Matrix Sum

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Math   

---

## Problem Description

You are given an `n x n` integer `matrix`. You can do the following operation **any** number of times:
    - Choose any two **adjacent** elements of `matrix` and **multiply** each of them by `-1`.
Two elements are considered **adjacent** if and only if they share a **border**.

Your goal is to **maximize** the summation of the matrix's elements. Return the **maximum** sum of the matrix's elements using the operation mentioned above.
---

## Examples
Example 1:
```
Input: matrix = [[1,-1],[-1,1]]
Output: 4
Explanation: We can follow the following steps to reach sum equals 4:
- Multiply the 2 elements in the first row by -1.
- Multiply the 2 elements in the first column by -1.
```
Example 2:
```
Input: matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
Output: 16
Explanation: We can follow the following step to reach sum equals 16:
- Multiply the 2 last elements in the second row by -1.
```

## Constraints

- `n == matrix.length == matrix[i].length`
- `2 <= n <= 250`
- `-10^5 <= matrix[i][j] <= 10^5`

---

## Approach: Math

### Intuition

Since we can perform the operation any number of times, we can always try to make all elements positive.
To maximize the sum, we should try to make as many elements as possible positive. 
If the number of negative elements is odd, then there will be one element that will be negative after all operations.
We should try to make this element as small as possible. 
If the number of negative elements is even, then all elements will be positive after all operations.
We can simply sum all elements in the matrix. 

If first case, we return `sum - abs_min * 2`
If second case, we return `sum`

### Complexity Analysis
Let `n` be the number of rows in the matrix and `m` be the number of columns in the matrix.
- **Time Complexity:** `O(n * m)`
- **Space Complexity:** `O(1)`

---

## Implementation

See `solution.py` for the full implementation.
