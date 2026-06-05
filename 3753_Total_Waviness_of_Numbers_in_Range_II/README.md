# 3753. Total Waviness of Numbers in Range II

**Difficulty:** <span style="color:#e74c3c"><b>Hard</b></span>  
**Topics:** Math, Dynamic Programming

---

## Problem Description

You are given two integers `num1` and `num2` representing an **inclusive** range `[num1, num2]`.

The **waviness** of a number is defined as the total count of its **peaks** and **valleys**:

- A digit is a **peak** if it is **strictly greater** than both of its immediate neighbors.
- A digit is a **valley** if it is **strictly less** than both of its immediate neighbors.
- The first and last digits of a number **cannot** be peaks or valleys.
- Any number with fewer than 3 digits has a waviness of 0.

Return the total sum of waviness for all numbers in the range `[num1, num2]`.

---

## Examples

**Example 1:**
```
Input: num1 = 120, num2 = 130
Output: 3
```
**Explanation:**
In the range `[120, 130]`:
- `120`: middle digit 2 is a peak, waviness = 1.
- `121`: middle digit 2 is a peak, waviness = 1.
- `130`: middle digit 3 is a peak, waviness = 1.
All other numbers in the range have a waviness of 0.
Thus, total waviness is `1 + 1 + 1 = 3`.

**Example 2:**
```
Input: num1 = 198, num2 = 202
Output: 3
```
**Explanation:**
In the range `[198, 202]`:
- `198`: middle digit 9 is a peak, waviness = 1.
- `201`: middle digit 0 is a valley, waviness = 1.
- `202`: middle digit 0 is a valley, waviness = 1.
All other numbers in the range have a waviness of 0.
Thus, total waviness is `1 + 1 + 1 = 3`.

## Constraints

- `1 <= num1 <= num2 <= 10^15`

---

## Approach: Dynamic Programming (Digit DP)

### Intuition

This problem asks for the sum of "waviness" over a large range of numbers. A brute-force approach of iterating through each number would be too slow given the constraints (`num2` up to 10^15). This is a classic problem that can be solved efficiently using **Digit Dynamic Programming**.

The core idea of Digit DP is to count numbers (or sum properties of numbers) up to a certain number `n` by building them digit by digit. To find the total waviness in a range `[num1, num2]`, we can calculate the total waviness for all numbers up to `num2` and subtract the total waviness for all numbers up to `num1 - 1`. That is, `totalWaviness(num1, num2) = calc(num2) - calc(num1 - 1)`.

We can define a recursive function, `dfs(pos, prev2, prev1, tight, started)`, to implement `calc(n)`. This function will count the numbers and sum their waviness from a given state.

The state of our DP is defined by:
- `pos`: The current digit position we are filling (from left to right).
- `prev2`, `prev1`: The previous two digits placed. We need these to check for peaks or valleys. We can use a special value (e.g., 10) to indicate that these digits don't exist yet.
- `tight`: A boolean flag. If `true`, it means we are restricted to the digits of `n` (i.e., the current digit can be from 0 to `n[pos]`). If `false`, the digit can be from 0 to 9.
- `started`: A boolean flag to handle leading zeros.

The `dfs` function needs to return two values for each state:
1.  `count`: The total count of valid numbers that can be formed from this state.
2.  `sum`: The total waviness accumulated by all those valid numbers.

In each recursive step, we iterate through the possible digits `d` for the current `pos`. For each `d`, we determine if it creates a new peak or valley with `prev1` and `prev2`. Let's say this adds `waviness_add` (0 or 1). We then recursively call `dfs` for the next position. The result from the recursive call, `child_state`, gives us the count and sum for the rest of the number.

The total waviness for the current branch is `child_state.sum` (the waviness from the suffix) plus `waviness_add * child_state.count` (the waviness we just created, multiplied by the number of ways the suffix can be formed).

By summing these up for all possible digits `d` and using memoization on the state `(pos, prev2, prev1, started)`, we can efficiently calculate the total waviness.

### Complexity Analysis

- **Time Complexity:** `O(log10(N))`, where `N` is the upper bound of the range. The number of states in our DP is approximately `pos * prev2 * prev1 * started * tight`, which is `log10(N) * 11 * 11 * 2 * 2`. For each state, we do a constant amount of work (a loop of at most 10). Therefore, the complexity is proportional to the number of digits in `N`.
- **Space Complexity:** `O(log10(N))` for the memoization table and the recursion stack.

---

## Implementation

See `solution.c++` for the full implementation.
