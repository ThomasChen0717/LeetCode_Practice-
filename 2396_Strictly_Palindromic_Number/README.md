# 2396. Strictly Palindromic Number

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Math, digit manipulation  

---

## Problem Description

An integer `n` is **strictly palindromic** if, for **every** base `b` between `2` and `n - 2` **(inclusive)**, the string representation of the integer `n` in base `b` is **palindromic**.

Given an integer `n`, return **true** if `n` is **strictly palindromic** and `false` otherwise.

A string is **palindromic** if it reads the same forward and backward.

---

## Examples
Example 1:
```
Input: n = 9
Output: false
Explanation: In base 2: 9 = 1001 (base 2), which is palindromic.
In base 3: 9 = 100 (base 3), which is not palindromic.
Therefore, 9 is not strictly palindromic so we return false.
Note that in bases 4, 5, 6, and 7, n = 9 is also not palindromic.
```
Example 2:
```
Input: n = 4
Output: false
Explanation: We only consider base 2: 4 = 100 (base 2), which is not palindromic.
Therefore, we return false.
```
## Constraints

- `4 <= n <= 10^5`

---

## Approach 1: Check Palindrome for each base 

### Intuition

Strictly palindromic number is a number that is palindromic in all bases from 2 to n-2. Therefore, we need to check if the number is palindromic in each base from 2 to n-2.

### Complexity Analysis

- **Time Complexity:** `O((n-2) * log n)`
- **Space Complexity:** `O(log n)`

---

## Approach 2: Math

### Intuition

For all `n >= 4`, the number is not strictly palindromic. Because in base `n-2`, the number is always `12`.
- `n= 1 * (n−2) + 2`



### Complexity Analysis

- **Time Complexity:** `O(1)`
- **Space Complexity:** `O(1)`

---

## Implementation

See `solution.py` for the full implementation.
