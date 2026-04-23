# 2615. Sum of Distances

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Array, Hash Table, Prefix Sum

---

## Problem Description

You are given a 0-indexed integer array `nums`. There exists an array `arr` of length `nums.length`, where `arr[i]` is the sum of `|i - j|` over all `j` such that `nums[j] == nums[i]` and `j != i`. If there is no such `j`, set `arr[i]` to be 0.

Return the array `arr`.

---

## Examples

**Example 1:**
```
Input: nums = [1,3,1,1,2]
Output: [5,0,3,4,0]
```
**Explanation:**
- When `i = 0`, `nums[0] == nums[2]` and `nums[0] == nums[3]`. Therefore, `arr[0] = |0 - 2| + |0 - 3| = 5`.
- When `i = 1`, `arr[1] = 0` because there is no other index with value 3.
- When `i = 2`, `nums[2] == nums[0]` and `nums[2] == nums[3]`. Therefore, `arr[2] = |2 - 0| + |2 - 3| = 3`.
- When `i = 3`, `nums[3] == nums[0]` and `nums[3] == nums[2]`. Therefore, `arr[3] = |3 - 0| + |3 - 2| = 4`.
- When `i = 4`, `arr[4] = 0` because there is no other index with value 2.

**Example 2:**
```
Input: nums = [0,5,3]
Output: [0,0,0]
```
**Explanation:** Since each element in `nums` is distinct, `arr[i] = 0` for all `i`.

## Constraints

- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^9`

---

## Approach 1: Brute Force

### Intuition

The most direct way to solve the problem is to follow the definition. For each element `nums[i]`, we can iterate through the entire array again to find all other indices `j` where `nums[j]` is equal to `nums[i]`. For each such `j`, we calculate the absolute difference `|i - j|` and add it to a running total. After checking all other elements, the total sum is the value for `arr[i]`.

This involves first grouping all indices by their corresponding number. A hash map is a good way to do this. Then, for each element `nums[i]`, we retrieve the list of indices for that number and compute the sum of distances.

### Complexity Analysis

- **Time Complexity:** `O(N^2)`, where `N` is the length of `nums`. For each element, we might iterate through a list of indices that, in the worst case, could be of length `N`. This makes the approach too slow for the given constraints.
- **Space Complexity:** `O(N)` to store the hash map of indices.

---

## Approach 2: Prefix Sum

### Intuition

The brute-force approach is inefficient because it repeatedly calculates sums. We can optimize this by pre-calculating sums. The key idea is to process elements in groups based on their value.

First, we group all indices for each unique number using a hash map, just like in the brute-force approach. Let's say for a certain number, the indices are `[idx_1, idx_2, ..., idx_k]` in sorted order.

For any given index `idx_i` in this list, the total distance is the sum of distances to all indices on its left plus the sum of distances to all indices on its right.
- Sum of distances to the left: `(idx_i - idx_1) + (idx_i - idx_2) + ... + (idx_i - idx_{i-1})`
- Sum of distances to the right: `(idx_{i+1} - idx_i) + (idx_{i+2} - idx_i) + ... + (idx_k - idx_i)`

These expressions can be rewritten using prefix sums. Let `P` be the prefix sum array for the list of indices. `P[i]` would be `idx_1 + ... + idx_i`.

- The sum of distances to the left can be calculated as: `i * idx_i - (P[i-1])`
- The sum of distances to the right can be calculated as: `(P[k-1] - P[i]) - (k - 1 - i) * idx_i`

By pre-calculating the prefix sums for each group of indices, we can find the total distance for each index in `O(1)` time. The overall process involves grouping indices and then iterating through each group to calculate prefix sums and then the final distances.

### Complexity Analysis

- **Time Complexity:** `O(N)`, where `N` is the length of `nums`. The initial grouping of indices takes `O(N)`. Then, we iterate through each group. Since the total number of elements across all groups is `N`, calculating prefix sums and the final distances for all elements also takes `O(N)` time in total.
- **Space Complexity:** `O(N)` to store the hash map and the resulting `arr`.

---

## Implementation

See `solution.py` for the full implementation of both approaches.
