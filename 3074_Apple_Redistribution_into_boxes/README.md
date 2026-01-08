# 3074. Apple Redistribution into Boxes

**Difficulty:** <span style="color:#2ecc71"><b>Easy</b></span>  
**Topics:** Array, Greedy, Sorting

---

## Problem Description

You are given an array `apple` of size `n` and an array `capacity` of size `m`.

There are `n` packs where the `ith` pack contains `apple[i]` apples. There are `m` boxes as well, and the `ith` box has a capacity of `capacity[i]` apples. 

Return the **minimum** number of boxes you need to select to redistribute these `n` packs of apples into boxes. 

**Note** that, apples from the same pack can be distributed into different boxes.

 

---

## Examples
Example 1:
```
Input: apple = [1,3,2], capacity = [4,3,1,5,2]
Output: 2
Explanation: We will use boxes with capacities 4 and 5.
It is possible to distribute the apples as the total capacity is greater than or equal to the total number of apples.
```
Example 2:
```
Input: apple = [5,5,5], capacity = [2,4,2,7]
Output: 4
Explanation: We will need to use all the boxes.
```

## Constraints

- `1 <= n == apple.length <= 50`
- `1 <= m == capacity.length <= 50`
- `1 <= apple[i], capacity[i] <= 50`
- The input is generated such that it's possible to redistribute packs of apples into boxes.

---

## Approach: Greedy

### Intuition

Since we want to minimize the number of boxes used, we should start with the boxes that have the largest capacity. We can sort the boxes in descending order of their capacity. 
Since all apples can be redistributed, we don't care about the original apple count in each pack. We only care about the total number of apples. 

### Complexity Analysis
Let  `n` be the length of the `apple` array and `m` be the length of the `capacity` array.
- **Time Complexity:** `O(n + m log m)`
- **Space Complexity:** If the sort is performed in place, the space complexity is `O(1)`. Otherwise, it depends on the sorting implementation, which can range from `O(m)` to `O(log m)`.

---

## Implementation

See `solution.py` for the full implementation.
