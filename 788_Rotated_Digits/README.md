# 788. Rotated Digits

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Math, Dynamic Programming

---

## Problem Description

An integer `x` is a **good** if after rotating each digit individually by 180 degrees, we get a valid number that is different from `x`. Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. For example:
- 0, 1, and 8 rotate to themselves.
- 2 and 5 rotate to each other.
- 6 and 9 rotate to each other.
- The rest of the numbers (3, 4, 7) do not rotate to any other number and become invalid.

Given an integer `n`, return the number of **good** integers in the range `[1, n]`.

---

## Examples

**Example 1:**
```
Input: n = 10
Output: 4
```
**Explanation:** There are four good numbers in the range [1, 10]: 2, 5, 6, 9. Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.

**Example 2:**
```
Input: n = 1
Output: 0
```

**Example 3:**
```
Input: n = 2
Output: 1
```

## Constraints

- `1 <= n <= 10^4`

---

## Approach 1: Brute Force

### Intuition

The most straightforward method is to iterate through every number from 1 to `n` and check if it's a "good" number. A number is good if it's valid after 180-degree rotation and is different from its original value.

To check a number, we can convert it to a string. Then, we check two conditions:
1.  It must not contain any invalid digits ('3', '4', '7').
2.  It must contain at least one of the digits that change to a different digit ('2', '5', '6', '9'). If it only contains digits that rotate to themselves ('0', '1', '8'), the rotated number will be the same as the original, so it won't be a "good" number.

If both conditions are met, we increment a counter.

### Complexity Analysis

- **Time Complexity:** `O(N * log10(N))`. We iterate through `N` numbers, and for each number, we convert it to a string, which takes `O(log10(N))` time.
- **Space Complexity:** `O(log10(N))` to store the string representation of the number.

---

## Approach 2: Dynamic Programming (Digit DP)

### Intuition

For larger constraints, a brute-force approach would be too slow. This problem can be optimized using Digit Dynamic Programming. The goal of Digit DP is to count numbers up to `n` that satisfy certain properties based on their digits.

We can define a recursive function, `dp(pos, tight, changed, started)`, that counts the number of ways to form a valid rotated number from a given position `pos` in the number `n` (represented as a string).

The state of our DP is defined by:
- `pos`: The current digit position we are filling (from left to right).
- `tight`: A boolean flag indicating if we are restricted to the digits of `n`. If `tight` is true, the current digit can be from 0 to `digits[pos]`. If false, it can be from 0 to 9.
- `changed`: A boolean flag that is true if we have used at least one "good" digit ('2', '5', '6', '9') so far.
- `started`: A boolean flag to handle leading zeros. It's true once we've placed a non-zero digit.

The function works as follows:
1.  **Base Case:** If `pos` reaches the end of the number, we have successfully formed a number. We return 1 if `changed` is true (meaning it's a "good" number), otherwise 0.
2.  **Memoization:** We use a memoization table to store the results for each state `(pos, tight, changed, started)` to avoid redundant computations.
3.  **Transitions:** We iterate through possible digits `d` for the current `pos`. The upper limit for `d` is `digits[pos]` if `tight` is true, otherwise it's 9.
    - We skip invalid digits ('3', '4', '7').
    - We update the `new_tight` flag: it remains true only if the original `tight` was true and we chose the maximum possible digit.
    - We update the `new_changed` flag: it becomes true if the original `changed` was true or if the current digit `d` is one of the "good" digits.
    - We recursively call the `dp` function for the next position with the updated state and add the result to our answer.

This DP approach systematically counts all "good" numbers up to `n` by building them digit by digit, respecting the upper bound `n`.

### Complexity Analysis

- **Time Complexity:** `O(log10(N))`. The number of states is roughly `pos * tight * changed * started`, which is `log10(N) * 2 * 2 * 2`. For each state, we do a constant amount of work (a loop of at most 10). Thus, the complexity is proportional to the number of digits in `N`.
- **Space Complexity:** `O(log10(N))` for the memoization table and recursion stack.

---

## Implementation

See `solution.py` for the full implementation of both approaches.
