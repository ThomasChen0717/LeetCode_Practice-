# 84_Largest_Rectangle_in_Histogram

**Difficulty:** <span style="color:#e74c3c"><b>Hard</b></span>  
**Topics:** Dynamic Programming, Stack  

---

## Problem Description

Given an array of `integers` heights representing the histogram's bar height where the width of each bar is `1`, return the area of the largest rectangle in the histogram.

---

## Examples
Example 1:
![Example 1](https://assets.leetcode.com/uploads/2021/01/04/histogram.jpg)
```
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
```
Example 2:
![Example 2](https://assets.leetcode.com/uploads/2021/01/04/histogram-1.jpg)
```
Input: heights = [2,4]
Output: 4
``` 

## Constraints

- `1 <= heights.length <= 10^5`
- `0 <= heights[i] <= 10^4`

---

## Approach 1: Brute Force

### Intuition

Iterate over each bar, iterate over each bar to the right of it, and find the minimum height between them by iteration. 
Then, calculate the area of the rectangle formed by the minimum height and the distance between the two bars.
Keep track of the maximum area found.
### Complexity Analysis

- **Time Complexity:** `O(n^3)`
- **Space Complexity:** `O(1)`

---

## Approach 2: Brute Force Improved

### Intuition

Same as Approach 1, but instead of using iteration to find the minimum height between two bars, we can keep track of the minimum height seen so far. 
Then, calculate the area of the rectangle formed by the minimum height and the distance between the current bar and the first bar with height less than the minimum height.
Keep track of the maximum area found.


### Complexity Analysis

- **Time Complexity:** `O(n^2)`
- **Space Complexity:** `O(1)`

---

## Approach 3: Divide and Conquer

### Intuition

We can use divide and conquer to solve this problem.
We can divide the histogram into three parts, and find the largest rectangle in each part.
    - The largest rectangle in the left part.
    - The largest rectangle in the right part.
    - The widest possible rectangle with height equal to the height of the shortest bar in the histogram.
We recursively divide the histogram into two parts centered on the shortest bar, and find the largest rectangle in each part, comparing it with the rectangle formed by the shortest bar.

### Complexity Analysis

- **Time Complexity:** `O(nlogn)` average case, `O(n^2)` worst case
- **Space Complexity:** `O(n)`

---

## Approach 4: Divide and Conquer with Segmented Tree

### Intuition

Same as Approach 3, but instead of using iteration to find the shortest bar, we can use a segmented tree to find the shortest bar in the histogram. Reduces the time complexity to `O(nlogn)`.

### Complexity Analysis

- **Time Complexity:** `O(nlogn)` 
- **Space Complexity:** `O(n)`

---

## Approach 5: Stack

### Intuition

We can use a stack to solve this problem.
We can iterate over each bar, and push the index of the bar into the stack if the height of the bar is greater than the height of the bar at the top of the stack.
If the height of the bar is less than or equal to the height of the bar at the top of the stack, we can pop the top of the stack, and calculate the area of the rectangle formed by the height of the popped bar and the distance between the current bar and the bar at the top of the stack.
Keep track of the maximum area found.

After iterating over all bars, if the stack is not empty, we can pop the top of the stack, and calculate the area of the rectangle formed by the height of the popped bar and the distance between the end of the histogram and the bar at the top of the stack.
Keep track of the maximum area found.

### Complexity Analysis

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

---

## Implementation

See `solution.py` for the full implementation.
