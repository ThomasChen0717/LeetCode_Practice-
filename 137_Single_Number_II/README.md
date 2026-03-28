# 137. Single Number II

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Bit Manipulation, Array

---

## Problem Description

Given an integer array `nums` where every element appears three times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.

---

## Examples

**Example 1:**
```
Input: nums = [2,2,3,2]
Output: 3
```

**Example 2:**
```
Input: nums = [0,1,0,1,0,1,99]
Output: 99
```

## Constraints

- `1 <= nums.length <= 3 * 10^4`
- `-2^31 <= nums[i] <= 2^31 - 1`
- Each element in `nums` appears exactly three times except for one element which appears once.

---

## Approach 1: Summing Bits

### Intuition

The problem asks us to find a single unique number in an array where all other numbers appear exactly three times. The constraints of linear time and constant space complexity rule out simple solutions like hash maps (which use extra space).

This problem is a variation of 136. Single Number, where every element appeared twice. In that case, a simple XOR operation worked perfectly. Here, with triplets, XOR alone won't suffice because `a ^ a ^ a = a`.

Instead, we can consider the bits of the numbers. If we sum the bits at each position (0 to 31) for all numbers in the array, the sum for each bit position will be a multiple of 3 if the unique number has a 0 at that bit. If the unique number has a 1 at that bit, the sum will be `3k + 1`.

By taking the sum of each bit position modulo 3, we can determine the corresponding bit of the unique number. If `sum % 3 == 1`, the unique number has a 1 at that bit position; otherwise, it has a 0.

The algorithm is as follows:
1. Initialize a variable `loner` to 0, which will be used to reconstruct the unique number.
2. Iterate through each bit position from 0 to 31.
3. For each bit position, calculate the sum of the bits of all numbers in the array.
4. Take this sum modulo 3. This result (`0` or `1`) is the bit of the unique number at the current position.
5. Set this bit in the `loner` variable by left-shifting it into the correct position and using a bitwise OR.
6. After iterating through all bits, `loner` will hold the unique number. A final check is needed to handle negative numbers correctly in Python's two's complement representation.

### Complexity Analysis

- **Time Complexity:** `O(N)`. Although we have a nested loop, the outer loop runs a fixed 32 times (for 32-bit integers), and the inner loop runs `N` times. Thus, the complexity is `O(32 * N)`, which simplifies to `O(N)`.
- **Space Complexity:** `O(1)`. We only use a few variables to store the bit sum and the result, requiring constant extra space.

---

## Approach 2: Generalized Bit Manipulation

### Intuition

This is a more abstract and highly efficient bit manipulation approach that processes the array in a single pass without an outer loop for bits. It uses two variables, `seen_once` and `seen_twice`, to keep track of the bits that have appeared once and twice, respectively.

The core idea is to simulate a state machine for each bit. A bit can be in one of three states:
1.  Appeared once.
2.  Appeared twice.
3.  Appeared three times.

We can represent these states with two variables. Let's trace the state transitions for a single bit:
-   **First appearance:** The bit is added to `seen_once` and not to `seen_twice`.
-   **Second appearance:** The bit is removed from `seen_once` and added to `seen_twice`.
-   **Third appearance:** The bit is removed from `seen_twice` (and is not in `seen_once`).

This logic can be implemented with the following bitwise formulas for each `num` in `nums`:
-   `seen_once = (seen_once ^ num) & (~seen_twice)`: This updates `seen_once`. A bit is added to `seen_once` if it's a new bit (`^ num`) but only if it wasn't already in `seen_twice`.
-   `seen_twice = (seen_twice ^ num) & (~seen_once)`: This updates `seen_twice`. A bit is added to `seen_twice` if it appeared once before (`^ num`) but only if it's not currently in the (newly updated) `seen_once`.

After iterating through all the numbers, the `seen_once` variable will hold the number that appeared exactly once, as all bits from the numbers appearing three times will have been canceled out from both `seen_once` and `seen_twice`.

### Complexity Analysis

- **Time Complexity:** `O(N)`. We iterate through the input array only once.
- **Space Complexity:** `O(1)`. We only use two extra variables to store the states.

---

## Implementation

See `solution.py` for the full implementation of both approaches.
