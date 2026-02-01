# 268 Missing Number

**Difficulty:** <span style="color:#2ecc71"><b>Easy</b></span>  
**Topics:** Sorting, HashSet, XOR, Gauss' Formula

---

## Problem Description

Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the only number in the range that is missing from the array.

---

## Examples
Example 1:
```
Input: nums = [3,0,1]

Output: 2

Explanation:

n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
```
Example 2:
```
Input: nums = [0,1]

Output: 2

Explanation:

n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
```
Example 3:
```
Input: nums = [9,6,4,2,3,5,7,0,1]

Output: 8

Explanation:

n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
```
## Constraints

- `n == nums.length`
- `1 <= n <= 10^4`
- `0 <= nums[i] <= n`
- All the numbers of `nums` are unique.

---

## Approach 1: Sorting

### Intuition

Simply sort the array and then check for the missing number.

### Complexity Analysis

- **Time Complexity:** `O(n log n)`
- **Space Complexity:** `O(n)` or `O(log n)` depending on the sorting algorithm.

---

## Approach 2: HashSet 

### Intuition

Use a HashSet to store the numbers in the array. Then, check for the missing number in the range `[0, n]`.

### Complexity Analysis

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

---

## Approach 3: XOR 

### Intuition

Use the XOR operation to find the missing number. XOR all the numbers in the array with all the numbers in the range `[0, n]`. The result will be the missing number.

This is because of XOR's property: 
- `a ^ a = 0`

Every number in the array will cancel out with its corresponding number in the range `[0, n]`, except for the missing number.

### Complexity Analysis

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

---

## Approach 4: Gauss' Formula

### Intuition

Use Gauss' formula to find the missing number. The formula is:

`missing_number = n * (n + 1) // 2 - sum(nums)`

### Complexity Analysis

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

---

## Implementation

See `solution.py` for the full implementation.
