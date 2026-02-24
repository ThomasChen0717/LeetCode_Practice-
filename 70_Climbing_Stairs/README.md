# 70. Climbing Stairs

**Difficulty:** <span style="color:#2ecc71"><b>Easy</b></span>  
**Topics:** Dynamic Programming, Fibonacci Number, Memoization

---

## Problem Description

You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?

---

## Examples
Example 1:
```
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
```
Example 2:
```
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```

## Constraints

- `1 <= n <= 45`

---

## Approach 1: Recursion with Memoization

### Intuition

We found that each subproblem `climb(curr)` depends on the results of `climb(curr + 1)` and `climb(curr + 2)`. Therefore, we can use recursion with memoization to avoid redundant calculations. 

Base cases:
- If `curr > n`, return `0`.
- If `curr == n`, return `1`.

### Complexity Analysis

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

---

## Approach 2: Dynamic Programming

### Intuition

We can use dynamic programming to solve this problem. We can define `dp[i]` as the number of distinct ways to climb to the `i`-th step. Then, we can have the following transition:

```
dp[i] = dp[i - 1] + dp[i - 2]
```

Base cases:
- `dp[0] = 1`
- `dp[1] = 1`

### Complexity Analysis

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

---

## Approach 3: Fibonacci Number

### Intuition

We can notice that `dp[i]` is actually the `i`-th Fibonacci number. Therefore, we can use the Fibonacci formula to calculate `dp[n]`.

### Complexity Analysis

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

---



## Implementation

See `solution.py` for the full implementation.
