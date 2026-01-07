# 415. Add Strings

**Difficulty:** <span style="color:#2ecc71"><b>Easy</b></span>  
**Topics:** Math, String

---

## Problem Description

Given two non-negative integers, `num1` and `num2` represented as string, return the sum of `num1` and `num2` as a string.

You must solve the problem without using any built-in library for handling large integers (such as `BigInteger`). You must also not convert the inputs to integers directly.

---

## Examples
Example 1:
```
Input: num1 = "11", num2 = "123"
Output: "134"
``` 

Example 2:
```
Input: num1 = "456", num2 = "77"
Output: "533"
``` 
Example 3:
```
Input: num1 = "0", num2 = "0"
Output: "0"
``` 
 

## Constraints

- `1 <= num1.length, num2.length <= 10^4`
- `num1` and `num2` consist of only digits.
- `num1` and `num2` don't have any leading zeros except for the zero itself.

---

## Approach: Math

### Intuition

Use the same approach as adding two numbers on paper. Start from the least significant digit and add corresponding digits along with any carry from the previous step.

### Complexity Analysis
Let `n` be the length of `num1` and `m` be the length of `num2`
- **Time Complexity:** O(max(n, m))
- **Space Complexity:** O(max(n, m))

---

## Implementation

See `solution.py` for the full implementation.
