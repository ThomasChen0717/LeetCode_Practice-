# 201. Bitwise AND of Numbers Range

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Bit Manipulation

---

## Problem Description

Given two integers `left` and `right` that represent the range `[left, right]`, return the bitwise AND of all numbers in this range, inclusive.

---

## Examples

**Example 1:**
```
Input: left = 5, right = 7
Output: 4
```
**Explanation:**
5 (binary `101`) & 6 (binary `110`) & 7 (binary `111`) = 4 (binary `100`).

**Example 2:**
```
Input: left = 0, right = 0
Output: 0
```

**Example 3:**
```
Input: left = 1, right = 2147483647
Output: 0
```

## Constraints

- `0 <= left <= right <= 2^31 - 1`

---

## Approach 1: Bit Shift

### Intuition

The bitwise AND of a range of numbers results in the common prefix of their binary representations. For any bit position where `left` and `right` differ, there must be at least one number in the range `[left, right]` that has a `0` at that bit position, making the final result have a `0` there as well.

Consider the range `[5, 7]`:
- 5: `101`
- 6: `110`
- 7: `111`

The common prefix is `1xx`. The final result will have `1` in the most significant bit and `0` for all the differing bits, resulting in `100` (which is 4).

This approach finds the common prefix by repeatedly right-shifting both `left` and `right` until they become equal. The number of shifts performed tells us how many of the rightmost bits were not part of the common prefix. We can then left-shift the common prefix back to its original position to get the final answer.

### Complexity Analysis

- **Time Complexity:** `O(log N)`, where `N` is the value of the numbers. The number of right shifts is limited by the number of bits in the integers (at most 32).
- **Space Complexity:** `O(1)`. We only use a few variables.

---

## Approach 2: Brian Kernighan's Algorithm

### Intuition

This approach also leverages the idea of finding a common prefix. The key insight is that the bitwise AND of the range `[left, right]` will be a number `x` such that `left <= x <= right` and `x` is a prefix of all numbers in the range.

The Brian Kernighan's algorithm provides a clever trick to turn off the rightmost set bit of a number `n` using the expression `n & (n - 1)`.

Example: `n = 6` (binary `110`)
- `n - 1 = 5` (binary `101`)
- `n & (n - 1) = 110 & 101 = 100` (4). The rightmost `1` is turned off.

We can apply this repeatedly to `right`. In each step, we are effectively removing a `1` from the right end. We continue this process as long as `right` is greater than `left`. Why does this work? Every time we apply `n & (n - 1)`, we are clearing the least significant bit that could possibly differ between `right` and some other number in the range. By continuing until `right <= left`, we ensure that `right` has been reduced to the common binary prefix of the entire range.

### Complexity Analysis

- **Time Complexity:** `O(log N)`. The number of iterations is at most the number of set bits in `right`, which is at most the number of bits in the integer (32).
- **Space Complexity:** `O(1)`. We only modify the `right` variable in-place.

---

## Implementation

See `solution.py` for the full implementation of both approaches.
