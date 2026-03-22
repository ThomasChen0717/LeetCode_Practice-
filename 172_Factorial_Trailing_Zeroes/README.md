# 172. Factorial Trailing Zeroes

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Math

---

## Problem Description

Given an integer `n`, return the number of trailing zeroes in `n!`.

Note that `n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1`.

---

## Examples

**Example 1:**
```
Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.
```

**Example 2:**
```
Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.
```

**Example 3:**
```
Input: n = 0
Output: 0
```

## Constraints

- `0 <= n <= 10^4`

---

## Approach 1: Counting Factors of 5

### Intuition

A trailing zero in a factorial is created by a factor of 10. Since `10 = 2 * 5`, we need to count the pairs of 2s and 5s in the prime factorization of `n!`. The number of factors of 2 will always be greater than or equal to the number of factors of 5. Therefore, the number of trailing zeros is determined by the number of factors of 5.

This approach iterates through all numbers from 5 to `n` and, for each number, counts how many times it is divisible by 5. For example, 25 contributes two 5s (`5 * 5`), and 125 contributes three 5s (`5 * 5 * 5`).


### Complexity Analysis

- **Time Complexity:** `O(n)`. The outer loop runs `n/5` times, and the inner `while` loop runs `log5(i)` times for each `i`. However, the inner loop time complexity is negligible compared to the outer loop, so the overall time complexity is `O(n)`. 
- **Space Complexity:** `O(1)`.

---

## Approach 2: Counting Factors of 5 (Optimal)

### Intuition

This is a more efficient way to count the factors of 5. Instead of checking every number, we can directly count how many multiples of 5, 25, 125, etc., exist up to `n`.

- Numbers that are multiples of 5 contribute at least one factor of 5. There are `n // 5` such numbers.
- Numbers that are multiples of 25 contribute an additional factor of 5 (since `25 = 5 * 5`). There are `n // 25` such numbers.
- Numbers that are multiples of 125 contribute yet another factor of 5. There are `n // 125` such numbers.

We continue this process, summing up the counts for all powers of 5 that are less than or equal to `n`. This gives the total count of factors of 5 in `n!`.

This method avoids redundant checks and achieves a logarithmic time complexity, as requested in the problem's follow-up.

### Complexity Analysis

- **Time Complexity:** `O(log n)`. Specifically, `O(log5 n)`, because we are dividing `n` by 5 in each step.
- **Space Complexity:** `O(1)`.

---

## Implementation

See `solution.py` for the full implementation of both approaches.
