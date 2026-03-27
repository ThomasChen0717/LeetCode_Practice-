# 136. Single Number

**Difficulty:** <span style="color:#2ecc71"><b>Easy</b></span>  
**Topics:** Bit Manipulation, Array

---

## Problem Description

Given a non-empty array of integers `nums`, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

---

## Examples

**Example 1:**
```
Input: nums = [2,2,1]
Output: 1
```

**Example 2:**
```
Input: nums = [4,1,2,1,2]
Output: 4
```

**Example 3:**
```
Input: nums = [1]
Output: 1
```

## Constraints

- `1 <= nums.length <= 3 * 10^4`
- `-3 * 10^4 <= nums[i] <= 3 * 10^4`
- Each element in the array appears twice except for one element which appears only once.

---

## Approach: Bit Manipulation (XOR)

### Intuition

The problem requires us to find the single element in an array where every other element appears exactly twice. The constraints are strict: linear time complexity (`O(N)`) and constant space complexity (`O(1)`).

A hash map could count frequencies, but that would use `O(N)` space. The key to a constant space solution lies in the properties of the bitwise XOR operation:
1.  **`a ^ a = 0`**: XORing a number with itself results in zero.
2.  **`a ^ 0 = a`**: XORing a number with zero results in the number itself.
3.  **`a ^ b = b ^ a`** (Commutative): The order of operands does not matter.
4.  **`(a ^ b) ^ c = a ^ (b ^ c)`** (Associative): The grouping of operands does not matter.

If we XOR all the numbers in the array together, the pairs of duplicate numbers will cancel each other out (e.g., `2 ^ 2 = 0`), leaving only the single, unique number.

For example, with `nums = [4, 1, 2, 1, 2]`:
The XOR sum would be `(4 ^ 1 ^ 2 ^ 1 ^ 2)`.
Due to the commutative and associative properties, we can reorder this as `4 ^ (1 ^ 1) ^ (2 ^ 2)`.
This simplifies to `4 ^ 0 ^ 0`, which equals `4`.

The algorithm is to simply initialize a variable to 0 and XOR it with every element in the array. The final result will be the single number.

### Complexity Analysis

- **Time Complexity:** `O(N)`, where `N` is the number of elements in the array. We iterate through the array once.
- **Space Complexity:** `O(1)`. We only use a single variable to store the accumulated XOR result, which is constant extra space.

---

## Implementation

See `solution.py`for the full implementation.
