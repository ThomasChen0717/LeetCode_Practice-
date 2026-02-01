# 9. Palindrome Number

**Difficulty:** <span style="color:#2ecc71"><b>Easy</b></span>  
**Topics:** Digit Manipulation, Math

---

## Problem Description

Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise.

---

## Examples
Example 1:
```
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
```
Example 2:
```
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
```
Example 3:
```
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
```

## Constraints

- `-2^31 <= x <= 2^31 - 1`

---

## Approach: Revert half of the number

### Intuition

First exclude the obvious cases: 
- If `x` is negative, it is not a palindrome.
- If `x` ends with 0, it is not a palindrome unless `x` is 0. 

Then we can build a new integer from the last digit of `x` and compare it with the first half of `x`.

If they are equal or `x` is equal to the reverted number divided by 10 (for odd number of digits), then `x` is a palindrome.

### Complexity Analysis

- **Time Complexity:** `O(log x)`
- **Space Complexity:** `O(1)`

---

## Implementation

See `solution.py` for the full implementation.
