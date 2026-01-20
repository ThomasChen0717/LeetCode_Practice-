# 167. Two Sum II - Input Array Is Sorted

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Array, Two Pointers

---

## Problem Description

Given a **1-indexed** array of integers `numbers` that is already **sorted in non-decreasing order**, find two numbers such that they add up to a specific `target` number. Let these two numbers be `numbers[index_1]` and `numbers[index_2]` where `1 <= index_1 < index_2 <= numbers.length`.

Return the indices of the two numbers, `index_1` and `index_2`, **added by one** as an integer array `[index_1, index_2]` of length 2.

The tests are generated such that there is **exactly one solution**. You **may not** use the same element twice.

Your solution must use only constant extra space.

---

## Examples
Example 1:
```
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
```
Example 2:
```
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
```
Example 3:
```
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
```
## Constraints

- `2 <= numbers.length <= 3 * 10^4`
- `-1000 <= numbers[i] <= 1000`
- `numbers` is sorted in **non-decreasing order**.
- `-1000 <= target <= 1000`
- The tests are generated such that there is **exactly one solution**.

---

## Approach: Two Pointers

### Intuition

Since the input is sorted, we can use the two-pointer technique to find the two numbers that add up to the target.
We initialize two pointers, `left` and `right`, at the beginning and end of the array, respectively.
We then move the pointers towards each other until we find the two numbers that add up to the target.
- If the sum of the numbers at the `left` and `right` pointers is less than the target, we increment the `left` pointer.
- If the sum of the numbers at the `left` and `right` pointers is greater than the target, we decrement the `right` pointer.
- If the sum of the numbers at the `left` and `right` pointers is equal to the target, we return the indices of the two numbers, `left + 1` and `right + 1`, as an integer array `[left + 1, right + 1]` of length 2.

### Complexity Analysis

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

---

## Implementation

See `solution.py` for the full implementation.
