# 42. Trapping Rain Water

**Difficulty:** <span style="color:#e74c3c"><b>Hard</b></span>  
**Topics:** Arrays, Dynamic Programming, Stack, Two Pointers

---

## Problem Description

Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

---

## Examples
Example 1:
```
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
```
Example 2:
```
Input: height = [4,2,0,3,2,5]
Output: 9
```

## Constraints

- `n == height.length`
- `1 <= n <= 2 * 10^4`
- `0 <= height[i] <= 10^5`

---

## Approach 1: Brute Force

### Intuition

For each of the heights, check its left and right max heights. The water trapped at each height is the minimum of the left and right max heights minus the height at that index.

### Complexity Analysis
Let `n` be the length of the height array.
- **Time Complexity:** `O(n^2)`
- **Space Complexity:** `O(1)`

---

## Approach 2: Dynamic Programming

### Intuition

Precompute the left and right max heights for each index. Then, for each index, the water trapped is the minimum of the left and right max heights minus the height at that index.

### Complexity Analysis
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

## Approach 3: Stack 

### Intuition

Use a stack to keep track of the indices of the heights. When a height is greater than the height at the top of the stack, it means we have found a potential trapping area. Calculate the water trapped and update the result.

### Complexity Analysis
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

---

## Approach 4: Two Pointers

### Intuition

Use two pointers to traverse the height array from both ends. We notice that when the height at the left is less than the right, then the water captured is bounded by the left height, and vice versa. 
We update the left and right pointers accordingly, and keep track of the left and right max heights seen so far. 

### Complexity Analysis
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

## Implementation

See `solution.py` for the full implementation.
