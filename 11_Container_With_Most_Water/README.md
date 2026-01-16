# 11. Container With Most Water

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Two Pointers, Array

---

## Problem Description

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `ith` line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

**Notice** that you may not slant the container.

---

## Examples
Example 1:
```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
````
Example 2:
```
Input: height = [1,1]
Output: 1
```

## Constraints

- `n == height.length`
- `2 <= n <= 10^5`
- `0 <= height[i] <= 10^4`

---

## Approach 1: Brute Force

### Intuition

Iterate through all possible pairs of lines and calculate the area formed by each pair. The maximum area found during this process is the answer.

### Complexity Analysis

- **Time Complexity:** `O(n^2)`
- **Space Complexity:** `O(1)`

---

## Approach 2: Two Pointers

### Intuition

Use two pointers, one starting from the left and the other from the right. Calculate the area formed by the lines at the current pointers and move the pointer pointing to the shorter line towards the other pointer. Keep track of the maximum area found during this process.

### Complexity Analysis

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

---

## Implementation

See `solution.py` for the full implementation.
