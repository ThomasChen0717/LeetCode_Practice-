# 50. Pow(x, n)

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Math, Recursion

---

## Problem Description

Implement `pow(x, n)`, which calculates `x` raised to the power `n` (i.e., `x^n`).

---

## Examples

**Example 1:**
```
Input: x = 2.00000, n = 10
Output: 1024.00000
```

**Example 2:**
```
Input: x = 2.10000, n = 3
Output: 9.26100
```

**Example 3:**
```
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25
```

## Constraints

- `-100.0 < x < 100.0`
- `-2^31 <= n <= 2^31 - 1`
- `n` is an integer.
- Either `x` is not zero or `n > 0`.
- `-10^4 <= x^n <= 10^4`

---

## Approach 1: Binary Exponentiation (Recursive)

### Intuition

The naive approach of multiplying `x` by itself `n` times is too slow, with a time complexity of `O(n)`. We can do much better using a divide-and-conquer strategy known as **binary exponentiation** or **exponentiation by squaring**.

The core idea is to use the properties of exponents:
- If `n` is even, `x^n = (x^2)^(n/2)`.
- If `n` is odd, `x^n = x * x^(n-1) = x * (x^2)^((n-1)/2)`.

This observation allows us to create a recursive function that halves the exponent `n` at each step, leading to a logarithmic time complexity. We must also handle the edge cases:
- If `n` is 0, the result is always 1.
- If `n` is negative, `x^n = 1 / x^(-n)`.

### Complexity Analysis

- **Time Complexity:** `O(log n)`. At each step, we reduce the exponent `n` by half.
- **Space Complexity:** `O(log n)`. This is due to the space consumed by the recursion call stack. The depth of the recursion is proportional to `log n`.

---

## Approach 2: Binary Exponentiation (Iterative)

### Intuition

We can also implement the binary exponentiation algorithm iteratively to avoid the overhead of the recursion stack. This approach relies on the binary representation of the exponent `n`.

The idea is to iterate while `n` is not zero. We maintain a `result` (initialized to 1) and the current power of `x` (which starts as `x` and gets squared in each iteration).

In each step of the loop:
1. Check if `n` is odd. If it is, it means the current power of `x` is needed for the final result, so we multiply `result` by `x`.
2. Square `x` to prepare for the next bit (e.g., from `x^1` to `x^2`, then `x^4`, `x^8`, and so on).
3. Halve `n` (using integer division `// 2`) to process the next bit of the exponent.

We first handle the case where `n` is negative by making `n` positive and taking the reciprocal of `x`.

### Complexity Analysis

- **Time Complexity:** `O(log n)`. The loop runs as many times as there are bits in `n`, which is `log n`.
- **Space Complexity:** `O(1)`. We only use a few variables to store the intermediate results, resulting in constant extra space.

---

## Implementation

See `solution.py` for the full implementation of both approaches.
