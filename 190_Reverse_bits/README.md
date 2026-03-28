# 190. Reverse Bits

**Difficulty:** <span style="color:#2ecc71"><b>Easy</b></span>  
**Topics:** Bit Manipulation, Divide and Conquer

---

## Problem Description

Reverse bits of a given 32-bit unsigned integer.

---

## Examples

**Example 1:**
```
Input: n = 43261596 (00000010100101000001111010011100)
Output: 964176192 (00111001011110000010100101000000)
```

**Example 2:**
```
Input: n = 4294967293 (11111111111111111111111111111101)
Output: 3221225471 (10111111111111111111111111111111)
```

## Constraints

- The input must be a binary string of length 32

---

## Approach 1: Bit by Bit

### Intuition

This is the most straightforward approach. We can iterate through the 32 bits of the input integer `n`, one at a time, and build the reversed integer. 

We initialize a result `ret` to 0. We loop 32 times. In each iteration, we do the following:
1.  Get the last bit of `n` using the bitwise AND operation (`n & 1`).
2.  Left-shift this bit to its new position in the reversed integer. For the `i`-th bit of `n` (from the right), its new position is `31 - i`. We can keep a `power` variable, initialized to 31, and decrement it in each step.
3.  Add (or `OR`) this shifted bit to our `ret`.
4.  Right-shift `n` by 1 to process the next bit.

This effectively takes the bits from the right of `n` and places them on the right of `ret`, but since `ret` is being built from left to right effectively (by decreasing the power of the shift), the bits of `n` are reversed.

### Complexity Analysis

- **Time Complexity:** `O(1)`, since the loop runs a fixed 32 times for any 32-bit integer.
- **Space Complexity:** `O(1)`, as we only use a few variables.

---

## Approach 2: Byte by Byte with Memoization

### Intuition

This approach is a powerful optimization if the `reverseBits` function is called many times. Instead of reversing one bit at a time, we can reverse a whole byte (8 bits) at a time.

The idea is to break the 32-bit integer into its four constituent bytes. We can pre-compute or cache the reversed value for all 256 possible bytes. Then, to reverse the 32-bit integer, we reverse each of its four bytes and place them in their new, reversed positions.

For example, if the integer is `[Byte1, Byte2, Byte3, Byte4]`, the reversed integer will be `[reverse(Byte4), reverse(Byte3), reverse(Byte2), reverse(Byte1)]`.

The solution uses a dictionary `self.cache` for memoization. When reversing a byte, it first checks if the result is already cached. If not, it computes the reversed byte, stores it in the cache, and then uses it. The `reverseByte` function itself uses a clever bit manipulation trick to reverse a byte in a single, fast operation.

### Complexity Analysis

- **Time Complexity:** `O(1)`. We process the 32-bit integer in 4 fixed chunks (bytes). The byte reversal and cache lookup are constant time operations.
- **Space Complexity:** `O(1)`. The cache will store at most 256 entries, which is a constant amount of space.

---

## Approach 3: Mask and Shift (Divide and Conquer)

### Intuition

This is a classic, elegant, and highly efficient method that does not require loops or caching. It works by reversing the bits in a divide-and-conquer fashion.

The process is as follows:
1.  Swap adjacent bits.
2.  Swap adjacent 2-bit chunks.
3.  Swap adjacent 4-bit chunks.
4.  Swap adjacent 8-bit chunks (bytes).
5.  Swap adjacent 16-bit chunks.

Each step uses bit masks to isolate the chunks that need to be swapped and bit shifts to move them to their new positions. For example, to swap adjacent bits, we can mask all the even-positioned bits (`0xAAAAAAAA`), shift them right by 1, and mask all the odd-positioned bits (`0x55555555`), shift them left by 1, and then combine them with `OR`.

This process is repeated with increasingly larger chunk sizes and shift amounts until the entire 32-bit integer is reversed.

### Complexity Analysis

- **Time Complexity:** `O(1)`, as it involves a fixed number of bitwise operations regardless of the input value.
- **Space Complexity:** `O(1)`. The reversal is done in-place.

---

## Implementation

See `solution.py` for the full implementation of all three approaches.
