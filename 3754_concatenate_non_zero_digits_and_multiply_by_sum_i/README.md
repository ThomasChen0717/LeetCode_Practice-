# 3754. Concatenate Non-Zero Digits and Multiply by Sum

**Difficulty:** <span style="color:#2ecc71"><b>Easy</b></span>  
**Topics:** Math, Digit Manipulation

---

## Problem Description

Given an integer `n`, you need to perform two calculations:

1.  Create a new integer `x` by concatenating all the non-zero digits of `n` in their original order.
2.  Calculate the sum `sm` of all the non-zero digits of `n`.

Return the product of `x` and `sm`.

---

## Examples

**Example 1:**
```
Input: n = 1203
Output: 738
Explanation:
- The non-zero digits are 1, 2, and 3.
- The concatenated number `x` is 123.
- The sum of non-zero digits `sm` is 1 + 2 + 3 = 6.
- The result is 123 * 6 = 738.
```

**Example 2:**
```
Input: n = 4050
Output: 405
Explanation:
- The non-zero digits are 4 and 5.
- The concatenated number `x` is 45.
- The sum of non-zero digits `sm` is 4 + 5 = 9.
- The result is 45 * 9 = 405.
```

**Example 3:**
```
Input: n = 5
Output: 25
Explanation:
- The non-zero digit is 5.
- The concatenated number `x` is 5.
- The sum of non-zero digits `sm` is 5.
- The result is 5 * 5 = 25.
```

## Constraints

- `1 <= n <= 10^9`

---

## Approach: Digit Manipulation

### Intuition

The problem requires us to process the digits of a given number `n`. We need to separate the non-zero digits to form a new number and calculate their sum. A straightforward way to do this is to iterate through the digits of `n` one by one.

We can extract digits from right to left using the modulo (`% 10`) and integer division (`// 10`) operators. As we process each digit, we can simultaneously build the concatenated number `x` and update the sum `sm`.

Since we are extracting digits from right to left, we need to be careful when constructing the new number `x`. For example, if `n = 123`, we will get `3`, then `2`, then `1`. To form `123`, we need to place each new digit at the most significant position of the number we are building. We can manage this by keeping track of the place value (using powers of 10).

### Algorithm

1.  Initialize three variables:
    -   `x = 0`: To store the concatenated number from non-zero digits.
    -   `sm = 0`: To store the sum of non-zero digits.
    -   `idx = 0`: To keep track of the decimal place for constructing `x`.

2.  Loop while `n` is greater than 0:
    a.  Extract the rightmost digit: `digit = n % 10`.
    b.  Remove the rightmost digit from `n`: `n //= 10`.
    c.  Check if the `digit` is not zero.
    d.  If the digit is non-zero:
        i.  Add it to the sum: `sm += digit`.
        ii. Prepend the digit to `x`. This can be done by `x = digit * (10 ** idx) + x`. For each non-zero digit we find, `idx` increases, correctly placing the next non-zero digit to its left.
        iii. Increment the place value index: `idx += 1`.

3.  After the loop finishes, return the product `x * sm`.

### Complexity Analysis

-   **Time Complexity:** `O(log10(n))`. The number of iterations in the loop is equal to the number of digits in `n`.
-   **Space Complexity:** `O(1)`. We only use a few variables to store the intermediate results, regardless of the size of `n`.

---

## Implementation

See `solution.py` for the full implementation.