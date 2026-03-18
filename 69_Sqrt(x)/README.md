# 69. Sqrt(x)

**Difficulty:** <span style="color:#2ecc71"><b>Easy</b></span>  
**Topics:** Math, Binary Search

---

## Problem Description

Given a non-negative integer `x`, return the square root of `x` rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.
- For example, do not use `pow(x, 0.5)` in c++ or `x ** 0.5` in python.

---

## Examples
**Example 1:** 
```
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
```

**Example 2:**
```
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
```

## Constraints

- `0 <= x <= 2^31 - 1`

---

## Approach 1: Binary Search

### Intuition

The problem asks for the integer `r` such that `r*r <= x` and `(r+1)*(r+1) > x`. The possible values for `r` are in the range `[0, x]`. Since this range is sorted, we can use binary search to find the answer efficiently.

We can define our search space from `2` to `x // 2` (since for `x > 1`, the square root is always less than `x/2`). We check the middle element `mid`. 
- If `mid*mid > x`, the actual root must be smaller than `mid`, so we search in the left half.
- If `mid*mid <= x`, `mid` could be our answer, or the answer could be larger. So we search in the right half, including `mid`.

We continue this process until the search space converges, and the result will be the largest integer whose square is less than or equal to `x`.

### Complexity Analysis

- **Time Complexity:** `O(log x)`. The search space is halved in each step.
- **Space Complexity:** `O(1)`. We only use a few variables.

---

## Approach 2: Recursion with Bit Shifts

### Intuition

This is a clever approach based on a recursive relationship. The core idea is that `sqrt(x)` is related to `sqrt(x/4)`. Specifically, `sqrt(x) = 2 * sqrt(x/4)`.

We can express this with bit shifts, as shifting right by 2 (`x >> 2`) is equivalent to dividing by 4, and shifting left by 1 (`y << 1`) is equivalent to multiplying by 2. 

The recursive formula is: `mySqrt(x) ≈ 2 * mySqrt(x/4)`. In terms of bit shifts: `mySqrt(x) ≈ mySqrt(x >> 2) << 1`.

Let `left = mySqrt(x >> 2) << 1`. The actual integer square root of `x` is either `left` or `left + 1`. We can simply check which one is correct: if `(left + 1) * (left + 1) > x`, then the answer is `left`; otherwise, it's `left + 1`.

The base case for the recursion is when `x < 2`, where `mySqrt(x)` is just `x`.

### Complexity Analysis

- **Time Complexity:** `O(log x)`. Each recursive step reduces `x` by a factor of 4, so the depth of recursion is `log4(x)`, which is proportional to `log x`.
- **Space Complexity:** `O(log x)` for the recursion call stack.

---

## Approach 3: Newton's Method

### Intuition

Newton's method is a classic numerical algorithm to find successively better approximations to the roots of a real-valued function. To find the square root of `x`, we are looking for the root of the function `f(y) = y^2 - x`.

The iterative formula for Newton's method is:
`y_new = y_old - f(y_old) / f'(y_old)`

For our function `f(y) = y^2 - x`, the derivative `f'(y) = 2y`. Substituting these into the formula, we get:
`y_new = y_old - (y_old^2 - x) / (2 * y_old)`
`y_new = (2*y_old^2 - y_old^2 + x) / (2 * y_old)`
`y_new = (y_old^2 + x) / (2 * y_old)`
`y_new = 0.5 * (y_old + x / y_old)`

We can start with an initial guess, say `y = x`, and repeatedly apply this formula. The value of `y` will converge to the square root of `x`. We can stop when the difference between `y_new` and `y_old` is less than some small epsilon (in this case, since we need an integer, we can stop when the difference is less than 1).

### Complexity Analysis

- **Time Complexity:** `O(log x)`. Newton's method converges quadratically, which means the number of correct digits roughly doubles with each iteration. The number of iterations is very small and proportional to `log(log x)`, but each iteration involves division, making the overall complexity closer to `O(log x)` depending on the implementation of division.
- **Space Complexity:** `O(1)`.

---

## Implementation

See `solution.py` for the full implementation of all three approaches.
