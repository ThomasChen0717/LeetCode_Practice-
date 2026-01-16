# Reverse Integer

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>      
**Topics:** Math, digit manipulation

---

## Problem Description

Given a signed 32-bit integer `x`, return `x` with its digits reversed. If reversing `x` causes the value to go outside the signed 32-bit integer range `[-2^31, 2^31 - 1]`, then return `0`.

**Assume the environment does not allow you to store 64-bit integers (signed or unsigned).**

---

## Examples
Example 1:
```
Input: x = 123
Output: 321
```
Example 2:
```
Input: x = -123
Output: -321
```
Example 3:
```
Input: x = 120
Output: 21
```

## Constraints

- `-2^31 <= x <= 2^31 - 1`

---

## Approach: Check for Overflow before Reversing

### Intuition

To reverse the digits of an integer, we can extract the digits one by one from the end and build the reversed number. However, we need to be careful to check for overflow before returning the result.

We can check at each step if `rev` is greater than `Integer.MAX_VALUE / 10` or less than `Integer.MIN_VALUE / 10` to detect overflow. 

If `rev` is greater than `Integer.MAX_VALUE / 10`, then appending the next digit would cause overflow.

If `rev` is less than `Integer.MIN_VALUE / 10`, then appending the next digit would cause overflow.

If `rev` is equal to `Integer.MAX_VALUE / 10` and the next digit is greater than `7`, then appending the next digit would cause overflow.

If `rev` is equal to `Integer.MIN_VALUE / 10` and the next digit is less than `-8`, then appending the next digit would cause overflow.

If overflow occurs, we return `0`.

### Complexity Analysis

- **Time Complexity:** `O(log(x))`
- **Space Complexity:** `O(1)`

---

## Implementation

See `solution.py` for the full implementation.
