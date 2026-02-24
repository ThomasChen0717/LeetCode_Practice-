# 3637. Trionic Array

**Difficulty:** <span style="color:#2ecc71"><b>Easy</b></span>  
**Topics:** Array

---

## Problem Description

You are given an integer array nums of length `n`.

An array is trionic if there exist indices `0 < p < q < n − 1` such that:

- `nums[0...p]` is **strictly** increasing,
- `nums[p...q]` is **strictly** decreasing,
- `nums[q...n − 1]` is **strictly** increasing.

Return `true` if `nums` is trionic, otherwise return `false`.

---

## Examples
Example 1:
```
Input: nums = [1,3,5,4,2,6]

Output: true

Explanation:

Pick p = 2, q = 4:

nums[0...2] = [1, 3, 5] is strictly increasing (1 < 3 < 5).
nums[2...4] = [5, 4, 2] is strictly decreasing (5 > 4 > 2).
nums[4...5] = [2, 6] is strictly increasing (2 < 6).
```
Example 2:
```
Input: nums = [2,1,3]

Output: false

Explanation:

There is no way to pick p and q to form the required three segments.
```

## Constraints

- `3 <= n <= 100`
- `0 <= nums[i] <= 1000`

---

## Approach 1: Evaluating Boundaries

### Intuition

We can solve this problem by simulating the path through the array and identifying the boundaries of each segment. The idea is to traverse the array three times, each time looking for one of the three required segments (increasing, decreasing, increasing).

The algorithm works as follows:
1.  **Find the first peak:** Traverse from the beginning of the array as long as it's strictly increasing. The point where it stops increasing is the first peak. If there's no initial increasing segment, it's not trionic.
2.  **Find the valley:** From the peak, traverse as long as the array is strictly decreasing. The point where it stops decreasing is the valley. If there's no decreasing segment or it goes to the end of the array, it's not trionic.
3.  **Find the final peak:** From the valley, traverse as long as the array is strictly increasing.
4.  If the traversal successfully reaches the end of the array after completing all three parts, the array is trionic. Otherwise, it is not.

### Complexity Analysis

- **Time Complexity:** `O(N)`, where `N` is the length of `nums`. We traverse the array with a single pointer `i`, so we visit each element at most once.
- **Space Complexity:** `O(1)`, as we only use a few variables to keep track of our position.

---

## Approach 2: Count Turning Points

### Intuition

A trionic array has a specific shape: `/\/`. This shape is defined by exactly two "turning points": a peak (where it changes from increasing to decreasing) and a valley (where it changes from decreasing to increasing).

This approach iterates through the array and counts these turning points:
1. First, validate that the array starts with a strictly increasing segment. If `nums[0] >= nums[1]`, it cannot be trionic.
2. Iterate from the third element to the end of the array, comparing each element `nums[i]` with its two predecessors, `nums[i-1]` and `nums[i-2]`.
3. A turning point occurs if the direction changes. This can be checked with the condition: `(nums[i-2] < nums[i-1] and nums[i-1] > nums[i])` (a peak) or `(nums[i-2] > nums[i-1] and nums[i-1] < nums[i])` (a valley).
4. We expect exactly two such turns. If we find more or fewer than two, the array is not trionic.

### Complexity Analysis

- **Time Complexity:** `O(N)`, as we perform a single pass through the array.
- **Space Complexity:** `O(1)`, using only a counter variable.

---

## Implementation

See `solution.py` for implementation details.
