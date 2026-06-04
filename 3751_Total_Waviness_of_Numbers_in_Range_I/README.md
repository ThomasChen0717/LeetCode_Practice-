# 3751. Total Waviness of Numbers in Range I

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Math, Dynamic Programming, Enumeration

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

- `1 <= num1 <= num2 <= 10^5`

---

## Approach 1: Enumeration

### Intuition

The most direct way to solve this problem is to iterate through every number in the given range `[num1, num2]` and calculate the "waviness" for each one. The total waviness is the sum of the waviness of all numbers in the range.

To calculate the waviness of a single number, we can inspect its digits. A digit is a peak or a valley only if it has two neighbors, so we only need to check the digits from the second to the second-to-last. We can iterate through the digits of the number, keeping track of the previous, current, and next digits to see if the current digit forms a peak or a valley.

This approach is simple to implement but may be slow if the range `[num1, num2]` is very large.

### Complexity Analysis

- **Time Complexity:** `O((num2 - num1) * log10(num2))`. We iterate through `num2 - num1` numbers, and for each number, we process its digits, which takes `O(log10)` time.
- **Space Complexity:** `O(log10(num2))` to store the digits of a number during the waviness calculation.

---

## Approach 2: Dynamic Programming (Digit DP)

### Intuition

When the range of numbers is large, a brute-force enumeration becomes too slow. This is a classic scenario for Digit Dynamic Programming. The core idea is to count the total waviness for all numbers up to `n` and then use this to find the total for a range. The total waviness in `[num1, num2]` is `calc(num2) - calc(num1 - 1)`.

We define a function `calc(n)` that computes the total waviness of all numbers from 1 to `n`. This is done with a recursive DFS function, `dfs(pos, prev2, prev1, tight, started)`, which builds the numbers digit by digit.

The state of our DP is defined by:
- `pos`: The current digit position we are filling (from left to right).
- `prev2`, `prev1`: The previous two digits placed. We need these to check for peaks/valleys.
- `tight`: A boolean flag indicating if we are restricted by the digits of `n`. If true, the current digit can be from 0 to `n[pos]`. If false, it can be 0-9.
- `started`: A boolean flag to handle leading zeros.

The `dfs` function returns a `State` object containing two pieces of information:
- `count`: The number of valid numbers that can be formed from the current state.
- `sum`: The total waviness of all those valid numbers.

In each step of the recursion, we iterate through the possible digits for the current position. For each digit, we calculate the new waviness contributed by this digit (if it forms a peak or valley with `prev1` and `prev2`). The total waviness for the current state is the sum of the waviness from the recursive calls (`child.sum`) plus the new waviness, which is `add * child.count` (the waviness `add` is 1 or 0, and it applies to all `child.count` numbers formed from the next state).

By using memoization on the state `(pos, prev2, prev1, started)`, we avoid re-computing results for the same subproblems.

### Complexity Analysis

- **Time Complexity:** `O(log10(N))`. The number of states is roughly `pos * prev2 * prev1 * started`, which is `log10(N) * 11 * 11 * 2`. For each state, we do a constant amount of work. The complexity is proportional to the number of digits in `N`.
- **Space Complexity:** `O(log10(N))` for the memoization table and recursion stack.

---

## Implementation

See `solution.c++` for the full implementation of both approaches.
