# 238. Product of Array Except Self

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Array, Prefix Product, Suffix Product

---

## Problem Description

Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.

You must write an algorithm that runs in `O(n)` time and without using the division operation.
---

## Examples
Example 1:
```
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
```
Example 2:
```
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
```

## Constraints

- `2 <= nums.length <= 10^5`
- `-30 <= nums[i] <= 30`
- The input is generated such that `answer[i]` is **guaranteed** to fit in a **32-bit** integer.

---

## Approach 1: Prefix Product and Suffix Product

### Intuition

We can calculate the product of all elements to the left of each index `i` and the product of all elements to the right of each index `i` using prefix product and suffix product.

At each index `i`, we can calculate the product of all elements to the left of `i` and the product of all elements to the right of `i` using prefix product and suffix product.

### Complexity Analysis
Let `n` be the length of the input array `nums`.
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

---

## Approach 2: Prefix Product and Suffix Product with Constant Space

### Intuition

We use `ans` to store either prefix or suffix product. 

We then compute the missing product on the fly.

### Complexity Analysis
Let `n` be the length of the input array `nums`.
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`



## Implementation

See `solution.py` for the full implementation.
