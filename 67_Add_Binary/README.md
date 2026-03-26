# 67. Add Binary

**Difficulty:** <span style="color:#2ecc71"><b>Easy</b></span>  
**Topics:** Math, String, Bit Manipulation

---

## Problem Description

Given two binary strings `a` and `b`, return their sum as a binary string.

---

## Examples

**Example 1:**
```
Input: a = "11", b = "1"
Output: "100"
```

**Example 2:**
```
Input: a = "1010", b = "1011"
Output: "10101"
```

## Constraints

- `1 <= a.length, b.length <= 10^4`
- `a` and `b` consist only of `'0'` or `'1'` characters.
- Each string does not contain leading zeros except for the zero itself.

---

## Approach 1: Bitwise Operation

### Intuition

Instead of simulating grade-school addition, we can leverage the power of bitwise operations to compute the sum. This approach treats the binary strings as actual numbers and uses bit manipulation to mimic how a computer's circuitry (a full adder) would perform the addition.

The core idea is to compute the sum in two parts:
1.  **Sum without carry:** The XOR (`^`) operation gives us the sum of two bits without considering the carry. For example, `1 ^ 1 = 0`, `1 ^ 0 = 1`.
2.  **Carry:** The AND (`&`) operation tells us where a carry is generated. A carry occurs only when both bits are 1 (`1 & 1 = 1`). We then left-shift this result by one (`<< 1`) to move the carry to the next position.

We can repeatedly apply these operations until the carry becomes zero. Let `x` be the current sum and `y` be the carry.

1.  Calculate `answer = x ^ y` (the sum of bits where at least one is not a 1).
2.  Calculate `carry = (x & y) << 1` (the bits that need to be carried over to the next position).
3.  Update `x = answer` and `y = carry`.
4.  Repeat until `y` (the carry) is zero.

This method elegantly handles the addition by separating the sum and carry calculations in each step.

### Complexity Analysis

- **Time Complexity:** `O(N + M)`, where `N` and `M` are the lengths of strings `a` and `b`. This accounts for converting the strings to integers. The `while` loop's iterations depend on the number of bits in the carry, which is at most `max(N, M)`. 
- **Space Complexity:** `O(max(N, M))` to store the result of the addition.

---

## Approach 2: Bit-by-Bit Addition

### Intuition

This approach mimics the way we manually add numbers on paper, from right to left. We process the binary strings one bit at a time, keeping track of a `carry` value as we go.

The algorithm is as follows:
1.  Pad the shorter string with leading zeros so that both strings have the same length. This simplifies the iteration.
2.  Initialize an empty list for the `answer` and a `carry` of 0.
3.  Iterate through the strings from the last character to the first.
4.  For each position, sum the integer values of the bits from both strings and add the current `carry`.
5.  The resulting bit for the current position is `sum % 2`. Append this to the `answer` list.
6.  The new `carry` for the next iteration is `sum // 2`.
7.  After the loop, if there is a remaining `carry` of 1, append it to the `answer`.
8.  Since we built the answer from right to left, reverse it and join the characters to form the final binary string.

### Complexity Analysis

- **Time Complexity:** `O(max(N, M))`, where `N` and `M` are the lengths of strings `a` and `b`. We iterate through the length of the longer string once.
- **Space Complexity:** `O(max(N, M))` to store the result string.

---

## Implementation

See `solution.py` for the full implementation of the full solution.
