# 2975. Maximum Square Area by Removing Fences From a Field

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Enumeration, Array, Hash Set

---

## Problem Description

There is a large `(m - 1) x (n - 1)` rectangular field with corners at `(1, 1)` and `(m, n)` containing some **horizontal** and **vertical** fences given in arrays `hFences` and `vFences` respectively.

**Horizontal** fences are from the coordinates `(hFences[i], 1)` to `(hFences[i], n)` and **vertical** fences are from the coordinates `(1, vFences[i])` to `(m, vFences[i])`.

Return the **maximum area** of a **square** field that can be formed by **removing some fences** (possibly none) or `-1` if it is impossible to make a **square** field.

Since the answer may be large, return it **modulo** `10^9 + 7`.

> **Note:** The field is surrounded by two **horizontal** fences from the coordinates `(1, 1)` to `(1, n)` and `(m, 1)` to `(m, n)` and two **vertical** fences from the coordinates `(1, 1)` to `(m, 1)` and `(1, n)` to `(m, n)`. These fences **cannot be removed**.


---

## Examples
Example 1:
![Example 1](https://assets.leetcode.com/uploads/2023/11/05/screenshot-from-2023-11-05-22-40-25.png)
```
Input: m = 4, n = 3, hFences = [2,3], vFences = [2]
Output: 4
Explanation: Removing the horizontal fence at 2 and the vertical fence at 2 will give a square field of area 4.
```
Example 2:

![Example 2](https://assets.leetcode.com/uploads/2023/11/22/maxsquareareaexample1.png)
``` 
Input: m = 6, n = 7, hFences = [2], vFences = [4]
Output: -1
Explanation: It can be proved that there is no way to create a square field by removing fences.
```
## Constraints

- `3 <= m, n <= 10^9`
- `1 <= hFences.length, vFences.length <= 600`
- `1 < hFences[i] < m`
- `1 < vFences[i] < n`
- All the elements in `hFences` are distinct.
- All the elements in `vFences` are distinct.

---

## Approach: Enumerate All Possible Squares

### Intuition

To obtain the largest possible square, we need the side length to be as large as possible.  
1. Collect all candidate horizontal gaps:  
   - Add the immutable borders 1 and m to hFences, sort, and compute every adjacent difference.  
2. Collect all candidate vertical gaps:  
   - Add the immutable borders 1 and n to vFences, sort, and compute every adjacent difference.  
3. Store these gaps in two hash sets for O(1) lookup.  
4. The maximum achievable side is the largest value that appears in both sets.  
5. If such a value exists, return its square modulo 1e9+7; otherwise return -1.  

### Complexity Analysis
Let `h` be the length of `hFences` and `v` be the length of `vFences`.
- **Time Complexity:** `O(h^2 + v^2)`
- **Space Complexity:** `O(h^2 + v^2)`

---

## Implementation

See `solution.py` for the full implementation.
