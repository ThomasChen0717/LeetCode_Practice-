# 149. Max Points on a Line

**Difficulty:** <span style="color:#e74c3c"><b>Hard</b></span>  
**Topics:** Hash Table, Math, Geometry

---

## Problem Description

Given an array of `points` where `points[i] = [xi, yi]` represents a point on the **X-Y** plane, return *the maximum number of points that lie on the same straight line*.

---

## Examples

**Example 1:**
![plane1](https://assets.leetcode.com/uploads/2021/02/25/plane1.jpg)
```
Input: points = [[1,1],[2,2],[3,3]]
Output: 3
```

**Example 2:**
![plane2](https://assets.leetcode.com/uploads/2021/02/25/plane2.jpg)
```
Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
```

## Constraints

- `1 <= points.length <= 300`
- `points[i].length == 2`
- `-10^4 <= xi, yi <= 10^4`
- All the points are **unique**.

---

## Approach: Normalized Slope

### Intuition

The fundamental idea is that all points on a single line share the same slope with respect to a common reference point. We can iterate through each point, treat it as an anchor, and calculate the slope it forms with every other point. By counting how many points share the same slope relative to the anchor, we can find the maximum number of points on any line originating from that anchor.

A key challenge is representing slopes accurately. Floating-point numbers can introduce precision errors. To avoid this, we represent the slope as a normalized fraction `(dy / dx)`. The normalization is done by dividing the difference in `y` (`dy`) and the difference in `x` (`dx`) by their greatest common divisor (GCD). This ensures that slopes like `2/4` and `1/2` are treated as identical.

Special cases must be handled:
- **Vertical Lines:** `dx = 0`. We can represent this with a unique slope tuple like `(0, 1)`.
- **Horizontal Lines:** `dy = 0`. This can be represented as `(1, 0)`.
- **Slope Sign:** To ensure consistency, we can enforce a rule that if `dx` is negative, we flip the signs of both `dx` and `dy`. This maps slopes like `1/-2` and `-1/2` to the same representation.

The overall algorithm is to iterate through each point `p1`, and for each `p1`, iterate through all subsequent points `p2`. We calculate the normalized slope between `p1` and `p2` and use a hash map to store the count of points for each slope. The maximum count found for any anchor point `p1` will give us the solution.

### Complexity Analysis

- **Time Complexity:** `O(N^2 * log(max(dx, dy)))`. We have a nested loop to iterate through all pairs of points (`O(N^2)`). For each pair, we calculate the GCD to normalize the slope. The Euclidean algorithm for GCD takes logarithmic time relative to the input values.
- **Space Complexity:** `O(N)`. For each anchor point, we use a hash map to store the slopes. In the worst-case scenario (all points form unique slopes with the anchor), the map could store up to `N-1` entries.

---

## Implementation

See `solution.py` for the full implementation.