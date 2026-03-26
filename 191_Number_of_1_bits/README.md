# 191. Number of 1 Bits

**Difficulty:** <span style="color:#2ecc71"><b>Easy</b></span>  
**Topics:** Bit Manipulation, Divide and Conquer

---

## Problem Description

Write a function that takes a positive integer `n` and returns the number of set bits in its binary representation (also known as the Hamming weight).

---

## Examples

**Example 1:**
```
Input: n = 11
Output: 3
Explanation: The input binary string 1011 has a total of three set bits.
```

**Example 2:**
```
Input: n = 128
Output: 1
Explanation: The input binary string 10000000 has a total of one set bit.
```

**Example 3:**
```
Input: n = 2147483645
Output: 30
Explanation: The input binary string 1111111111111111111111111111101 has a total of thirty set bits.
```

## Constraints

- `1 <= n <= 2^31 - 1`

---

## Approach 1: Loop and Flip

### Intuition

This is a straightforward approach where we check each of the 32 bits of the integer. We can use a bitmask to isolate each bit and check if it is a 1.

The algorithm is as follows:
1. Initialize a `count` to 0 and a `mask` to 1.
2. Loop 32 times (for a 32-bit integer).
3. In each iteration, perform a bitwise AND between the number `n` and the `mask`.
4. If the result is not zero, it means the bit at the mask's position is a 1, so we increment the `count`.
5. Left-shift the `mask` by one position (`mask <<= 1`) to check the next bit.
6. After the loop, `count` will hold the total number of set bits.

### Complexity Analysis

- **Time Complexity:** `O(1)`. The loop runs a fixed number of times (32), so the time taken is constant regardless of the input value.
- **Space Complexity:** `O(1)`. We only use a few variables to store the count and the mask.

---

## Approach 2: Bit Manipulation (Brian Kernighan's Algorithm)

### Intuition

This is a clever and highly efficient bit manipulation trick. The core idea is that for any integer `n`, the operation `n & (n - 1)` flips the least significant set bit (the rightmost '1') to a '0'.

For example:
- `n = 12` (binary `1100`)
- `n - 1 = 11` (binary `1011`)
- `n & (n - 1) = 1100 & 1011 = 1000` (binary `8`). The rightmost '1' has been turned off.

By repeatedly applying this operation and counting how many times we can do it before `n` becomes 0, we can find the total number of set bits.

### Complexity Analysis

- **Time Complexity:** `O(k)`, where `k` is the number of set bits (Hamming weight). In the worst case (a number like `2^31 - 1`), this is `O(1)` because `k` is at most 32.
- **Space Complexity:** `O(1)`.

---

## Approach 3: Divide by 2 and Check Remainder

### Intuition

This approach simulates converting the number to its binary representation. In base 2, dividing a number by 2 is equivalent to a right bit shift. The remainder of the division (`n % 2`) tells us the value of the least significant bit.

The algorithm is:
1. Initialize a `count` to 1.
2. While `n` is not zero:
   a. If `n % 2` is 1, it means the last bit is a '1', so increment `count`.
   b. Integer divide `n` by 2 (`n //= 2`) to discard the last bit.
3. Return `count`.

### Complexity Analysis

- **Time Complexity:** `O(log N)`. The number of divisions is proportional to the number of bits in `n`, which is `log2(N)`.
- **Space Complexity:** `O(1)`.

---

## Approach 4: Precompute Table (for frequent calls)

### Intuition

This approach is an optimization for scenarios where the `hammingWeight` function is called many times. The idea is to trade space for time by pre-computing the number of set bits for all possible 8-bit numbers (0-255) and storing them in a lookup table.

A 32-bit integer can be broken down into four 8-bit chunks (bytes). To find the total Hamming weight, we can look up the pre-computed count for each byte and sum them up.

The algorithm is as follows:
1.  **Pre-computation (done once):** Create a table of size 256. For each number `i` from 0 to 255, calculate its Hamming weight and store it in `table[i]`.
2.  **Lookup:** To get the Hamming weight of a 32-bit integer `n`:
    a. Get the count for the first byte: `table[n & 0xff]`
    b. Get the count for the second byte: `table[(n >> 8) & 0xff]`
    c. Get the count for the third byte: `table[(n >> 16) & 0xff]`
    d. Get the count for the fourth byte: `table[(n >> 24) & 0xff]`
    e. Sum these four values.

### Complexity Analysis

- **Time Complexity:** `O(1)`. The calculation involves four table lookups and three additions, which is constant time. The pre-computation is also a one-time constant cost.
- **Space Complexity:** `O(1)`. The lookup table has a fixed size of 256, which is constant.

---

## Implementation

See `solution.py` for the full implementation.
