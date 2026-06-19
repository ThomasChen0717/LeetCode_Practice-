# 1732. Find the Highest Altitude

**Difficulty:** <span style="color:#2ecc71"><b>Easy</b></span>  
**Topics:** Array, Prefix Sum

---

## Problem Description

There is a biker going on a road trip. The road trip consists of `n + 1` points at different altitudes. The biker starts his trip on point `0` with altitude equal `0`.

You are given an integer array `gain` of length `n` where `gain[i]` is the **net gain in altitude** between points `i`​​​​​​ and `i + 1` for all (`0 <= i < n)`. Return _the **highest altitude** of a point._

---

## Examples
Example 1: 
```
Input: gain = [-5,1,5,0,-7]
Output: 1
Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.
```

Example 2:
```
Input: gain = [-4,-3,-2,-1,4,3,2]
Output: 0
Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.
```

## Constraints

- `n == gain.length`
- `1 <= n <= 100`
- `-100 <= gain[i] <= 100`

---

## Approach

### Intuition

The problem asks for the highest altitude reached during a road trip. We start at an altitude of 0, and the `gain` array represents the net change in altitude between consecutive points.

This problem can be solved by keeping track of the current altitude as we traverse the `gain` array. We can initialize a `current_altitude` variable to 0, which is the starting altitude. We also need a `max_altitude` variable, also initialized to 0, to store the highest altitude seen so far.

We can then iterate through the `gain` array. For each gain, we add it to our `current_altitude`. After each update, we compare the `current_altitude` with `max_altitude` and update `max_altitude` if the `current_altitude` is higher.

This approach is essentially calculating the prefix sum of the `gain` array, with an initial value of 0, and finding the maximum value in the prefix sum array. However, we don't need to store the entire prefix sum array. We only need to keep track of the current sum and the maximum sum encountered.

### Complexity Analysis

- **Time Complexity:** `O(n)`, where `n` is the length of the `gain` array. We iterate through the array once.
- **Space Complexity:** `O(1)`. We only use a few variables to store the current and highest altitudes, so the space required is constant.

---

## Implementation

See `solution.c++` for the full implementation.
