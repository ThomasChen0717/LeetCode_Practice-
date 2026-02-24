# 169. Majority Element

**Difficulty:** <span style="color:#f39c12"><b>Easy</b></span>  
**Topics:** Arrays, Hash Table, Counting, Bit Manipulation

---

## Problem Description

Given an array `nums` of size `n`, return *the majority element*.

The majority element is the element that appears more than `n // 2` times. You may assume that the majority element always exists in the array.

---

## Examples
Example 1:
```
Input: nums = [3,2,3]
Output: 3
```
Example 2:
```
Input: nums = [2,2,1,1,1,2,2]
Output: 2
```

## Constraints

- `n == nums.length`
- `1 <= n <= 5 * 10^4`
- `-10^9 <= nums[i] <= 10^9`
- The input is generated such that a majority element will exist in the array.

---

## Approach 1: Hash Table

### Intuition

We can use a hash table to count the occurrences of each element in the array. Since the majority element appears more than `n // 2` times, it will be the key with the highest value in the hash table.

### Complexity Analysis

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

---

## Approach 2: Bit Manipulation

### Intuition

We can use bit manipulation to find the majority element. Since the majority element appears more than `n // 2` times, all of its set bits are setin more than half of the elements. We can count the number of `1`s at each bit position and if count exceeds `n // 2`, we set the corresponding bit in the majority element.  Note for python, we would need to handle negative case manually since its integer is not precision bounded. 

### Complexity Analysis

- **Time Complexity:** `O(n log C)` where `C` is the maximum absolute value in `nums`.
- **Space Complexity:** `O(1)`

---

## Approach 3: Boyer-Moore Voting Algorithm

### Intuition

We can use Boyer-Moore Voting Algorithm to find the majority element. The algorithm works by maintaining a candidate for the majority element and a count. Initially, the count is set to 0. We iterate through the array, and for each element:
- If the count is 0, we set the current element as the candidate.
- If the current element is the same as the candidate, we increment the count.
- Otherwise, we decrement the count.

Since the majority element appears more than `n // 2` times, it will survive the voting process.

### Complexity Analysis

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

---

## Implementation

See `solution.py` for the full implementation.
