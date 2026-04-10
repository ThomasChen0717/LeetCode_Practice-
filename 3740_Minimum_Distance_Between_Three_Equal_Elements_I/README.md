# 3740. Minimum Distance Between Three Equal Elements I

**Difficulty:** <span style="color:#f39c12"><b>Easy</b></span>  
**Topics:** Array, Hash Table

---

## Problem Description

You are given an integer array `nums`.

A tuple `(i, j, k)` of 3 distinct indices is **good** if `nums[i] == nums[j] == nums[k]`.

The **distance** of a good tuple is `abs(i - j) + abs(j - k) + abs(k - i)`, where `abs(x)` denotes the absolute value of `x`.

Return an integer denoting the minimum possible **distance** of a good tuple. If no good tuples exist, return -1.

---

## Examples

**Example 1:**
```
Input: nums = [1,2,1,1,3]
Output: 6
```
**Explanation:**
The minimum distance is achieved by the good tuple (0, 2, 3).
(0, 2, 3) is a good tuple because `nums[0] == nums[2] == nums[3] == 1`. Its distance is `abs(0 - 2) + abs(2 - 3) + abs(3 - 0) = 2 + 1 + 3 = 6`.

**Example 2:**
```
Input: nums = [1,1,2,3,2,1,2]
Output: 8
```
**Explanation:**
The minimum distance is achieved by the good tuple (2, 4, 6).
(2, 4, 6) is a good tuple because `nums[2] == nums[4] == nums[6] == 2`. Its distance is `abs(2 - 4) + abs(4 - 6) + abs(6 - 2) = 2 + 2 + 4 = 8`.

**Example 3:**
```
Input: nums = [1]
Output: -1
```
**Explanation:**
There are no good tuples. Therefore, the answer is -1.

## Constraints

- `1 <= n == nums.length <= 100`
- `1 <= nums[i] <= n`

---

## Approach: Hash Table

### Intuition

To find the minimum distance between three equal elements, we first need to find groups of three equal elements. A hash table (or a dictionary in Python) is a suitable data structure for this task. We can iterate through the input array `nums` and store the indices of each number in a list associated with that number as the key in the hash table.

Once we have the indices of each number grouped together, we can iterate through the values of the hash table. For each number that appears three or more times, we have a list of indices. The problem then reduces to finding the three indices `i`, `j`, and `k` from this list that minimize the distance formula: `abs(i - j) + abs(j - k) + abs(k - i)`.

If we sort the indices for a particular number, let's say `i < j < k`, the distance formula simplifies to `(j - i) + (k - j) + (k - i) = 2 * (k - i)`. To minimize this value, we need to minimize the difference between the largest and smallest index, `k - i`.

The most efficient way to do this is to consider a sliding window of size 3 over the sorted list of indices. For each window `[i, j, k]`, we calculate the distance and keep track of the minimum distance found so far.

The provided solution follows this logic by iterating through the `nums` array and using a dictionary `mp` to store the indices of each number. It maintains a list of the last three seen indices for each number. When a third index for a number is found, it calculates the distance for that triplet and updates the minimum distance. To keep the list of indices for each number at a maximum size of 3, it removes the oldest index when a new one is added beyond the third one. This is an optimization to avoid storing a long list of indices, which is not strictly necessary for this version of the problem but is a good practice.

### Complexity Analysis

- **Time Complexity:** `O(N)`, where `N` is the length of the `nums` array. We iterate through the array once.
- **Space Complexity:** `O(N)`, as in the worst case, all elements are unique, and we store one index for each.

---

## Implementation

See `solution.py` for the full implementation.
